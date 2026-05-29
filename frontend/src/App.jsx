import { useState } from 'react'
import './index.css'

function App() {
  const [jobDescription, setJobDescription] = useState('')
  const [file, setFile] = useState(null)
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0])
    }
  }

  const handleCalculateMatch = async (e) => {
    e.preventDefault()
    
    if (!jobDescription.trim() || !file) {
      setError('Please provide both a Job Description and upload a Resume file.')
      return
    }

    setLoading(true)
    setError(null)
    setResults(null)

    const formData = new FormData()
    formData.append('job_description', jobDescription)
    formData.append('file', file)

    try {
      const response = await fetch('http://127.0.0.1:5000/api/score', {
        method: 'POST',
        body: formData // Note: no Content-Type header so browser sets multipart/form-data boundary
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.error || 'Failed to calculate score')
      }

      setResults(data.results)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <div className="background-shapes">
        <div className="shape shape1"></div>
        <div className="shape shape2"></div>
      </div>

      <div className="container glass-panel">
        <header>
          <h1>AI Resume Parser</h1>
          <p>Find the perfect match using Natural Language Processing</p>
        </header>

        <form onSubmit={handleCalculateMatch}>
          <div className="form-group">
            <label htmlFor="jobDescription">Target Job Description</label>
            <textarea 
              id="jobDescription"
              rows="4" 
              placeholder="e.g., Seeking a Data Scientist with Python and NLP experience..."
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
            />
          </div>

          <div className="form-group file-upload-group">
            <label>Upload Candidates (.pdf, .docx, .txt, .zip)</label>
            <div className="file-dropzone">
              <input 
                type="file" 
                id="fileUpload" 
                accept=".pdf,.docx,.txt,.zip"
                onChange={handleFileChange}
              />
              <label htmlFor="fileUpload" className="file-label">
                {file ? file.name : "Choose a file or drag it here"}
              </label>
            </div>
          </div>
          
          <button type="submit" className="btn primary-btn" disabled={loading}>
            {loading ? <div className="spinner"></div> : <span>Calculate Match</span>}
          </button>
        </form>

        {error && (
          <div className="error-box">
            <p>{error}</p>
          </div>
        )}

        {results && !loading && (
          <div className="results-section">
            <h2>Leaderboard</h2>
            <div className="candidates-list">
              {results.map((candidate, index) => (
                <div key={index} className="candidate-card list-view fade-in" style={{animationDelay: `${index * 0.1}s`}}>
                  <div className="card-info">
                    <span className="rank">#{index + 1}</span>
                    <h3 className="filename">{candidate.filename}</h3>
                  </div>
                  <div className="score-display small">
                    <span className="score-number">{candidate.score}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </>
  )
}

export default App
