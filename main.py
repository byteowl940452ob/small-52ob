"""
Simple responsive component library.
Provides functions to generate basic HTML components.
"""

__all__ = ["card"]

def card(title, content, width="100%"):
    """Return a responsive card component."""
    return f"""
<div class="card" style="width:{width};margin:auto;">
  <h2>{title}</h2>
  <p>{content}</p>
</div>
<style>
.card {{ border:1px solid #ccc;padding:10px;box-sizing:border-box; }}
@media (max-width:600px) {{
  .card {{ width:100%; }}
}}
</style>
"""

if __name__ == "__main__":
    html = card("Hello", "This is a responsive card.")
    print(html)