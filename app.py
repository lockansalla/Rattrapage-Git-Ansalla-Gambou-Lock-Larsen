import gradio as gr

def message():
    return "Déploiement réussi via GitHub Actions CD vers Hugging Face Spaces !"

demo = gr.Interface(
    fn=message,
    inputs=[],
    outputs="text",
    title="🎓 Application Gradio - Rattrapage Git/GitHub - Ansalla Gambou"
)

if __name__ == "__main__":
    demo.launch()