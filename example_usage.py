from client import ReadabilityBoilerplateRemover

webpage = """
<nav>Home | Products | Contact</nav>
<div class="main">
    <p>Autonomous AI agents require persistent memory and deterministic tool calling.</p>
    <p>Ad: Buy GPUs now</p>
    <p>Mathematical proof verification ensures software correctness across formal systems.</p>
</div>
<footer>(c) 2026 Corporation</footer>
"""

clean_text = ReadabilityBoilerplateRemover.extract_main_content(webpage)
print("Substantive Main Content:\n" + clean_text)
