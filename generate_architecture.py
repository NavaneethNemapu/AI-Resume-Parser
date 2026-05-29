import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_box(ax, x, y, width, height, text, color='#E2E8F0', text_color='#0F172A', fontsize=12):
    # Draw rectangle with rounded corners effect using FancyBboxPatch
    box = patches.FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1,rounding_size=0.1", 
                                 edgecolor='#64748B', facecolor=color, lw=1.5)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, color=text_color, fontsize=fontsize, 
            ha='center', va='center', fontweight='bold', wrap=True)

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', arrowstyle='-|>,head_length=0.8,head_width=0.4', lw=2))

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Colors
    ui_color = '#E0F2FE' # Light Blue
    api_color = '#FEF3C7' # Light Sky
    ai_color = '#DCFCE7' # Light Amber
    db_color = '#F3E8FF' # Light Purple

    # Boxes
    draw_box(ax, 1, 4.5, 2.5, 0.8, "Recruiter\n(Web Browser)", '#F8FAFC')
    
    draw_box(ax, 1, 2.5, 2.5, 1.2, "React.js UI\n(Leaderboard &\nUploads)", ui_color)
    
    draw_box(ax, 5, 2.5, 2.5, 1.2, "Flask REST API\n(Python Server)", api_color)
    
    draw_box(ax, 5, 4.5, 2.5, 0.8, "PyPDF2 / docx\n(Extraction)", db_color)
    
    draw_box(ax, 5, 0.5, 2.5, 1.0, "NLTK Pipeline\n(Preprocessing)", ai_color)
    
    draw_box(ax, 8.5, 2.5, 1.2, 3.0, "AI Scoring\nEngine\n\n(TF-IDF &\nSet Match)", ai_color)

    # Arrows
    # Recruiter to UI
    draw_arrow(ax, 2.25, 4.4, 2.25, 3.8)
    draw_arrow(ax, 2.25, 3.8, 2.25, 4.4) # Two way
    
    # UI to API
    draw_arrow(ax, 3.6, 3.1, 4.9, 3.1)
    ax.text(4.25, 3.3, "JSON / Multipart", fontsize=9, ha='center', color='#64748B')
    draw_arrow(ax, 4.9, 2.9, 3.6, 2.9)
    
    # API to Extraction
    draw_arrow(ax, 6.25, 3.8, 6.25, 4.4)
    draw_arrow(ax, 6.25, 4.4, 6.25, 3.8)
    
    # API to NLTK
    draw_arrow(ax, 6.25, 2.4, 6.25, 1.6)
    draw_arrow(ax, 6.25, 1.6, 6.25, 2.4)
    
    # API to Scoring Engine
    draw_arrow(ax, 7.6, 3.1, 8.4, 3.1)
    draw_arrow(ax, 8.4, 2.9, 7.6, 2.9)

    plt.tight_layout()
    plt.savefig('architecture.png', dpi=300, bbox_inches='tight')
    print("Saved architecture.png")

if __name__ == '__main__':
    create_architecture_diagram()
