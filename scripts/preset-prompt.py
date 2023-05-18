import modules.scripts as scripts
import gradio as gr


class ExtensionTemplateScript(scripts.Script):
  # Extension title in menu UI
    def title(self):
        return "我在哪里"

    # Decide to show menu in txt2img or img2img
    # - in "txt2img" -> is_img2img is `False`
    # - in "img2img" -> is_img2img is `True`
    #
    # below code always show extension menu
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    # Setup menu ui detail
    def ui(self, is_img2img):
        with gr.Accordion('preset-prompt-我在这，快看呀，预设prompt', open=False):
            with gr.Row():
                checkbox = gr.Checkbox(
                    False,
                    label="Checkbox"
                )
        # TODO: add more UI components (cf. https://gradio.app/docs/#components)
        return [checkbox]

    # Extension main process
    # Type: (StableDiffusionProcessing, List<UI>) -> (Processed)
    # args is [StableDiffusionProcessing, UI1, UI2, ...]
    def run(self, p, checkbox):
        # TODO: get UI info through UI object angle, checkbox
        # proc = process_images(p)
        # TODO: add image edit process via Processed object proc
        return 1

















