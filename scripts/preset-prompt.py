import modules.scripts as scripts
import gradio as gr
from modules.processing import process_images

print(scripts.basedir())


class ExtensionTemplateScript(scripts.Script):
  # The title of the script. This is what will be displayed in the dropdown menu.
    def title(self):
        return "我在哪里"

    # Determines when the script should be shown in the dropdown menu via the 
    # returned value. As an example:
    # is_img2img is True if the current tab is img2img, and False if it is txt2img.
    # Thus, return is_img2img to only show the script on the img2img tab.
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    # How the script's is displayed in the UI. See https://gradio.app/docs/#components
    # for the different UI components you can use and how to create them.
    # Most UI components can return a value, such as a boolean for a checkbox.
    # The returned values are passed to the run method as parameters.
    def ui(self, is_img2img):
        with gr.Accordion('preset-prompt-我在这，快看呀，预设prompt', open=False):
            with gr.Row():
                checkbox = gr.Checkbox(
                    False,
                    label="Checkbox"
                )
        # TODO: add more UI components (cf. https://gradio.app/docs/#components)
        return [checkbox]

    # This is where the additional processing is implemented. The parameters include
    # self, the model object "p" (a StableDiffusionProcessing class, see
    # processing.py), and the parameters returned by the ui method.
    # Custom functions can be defined here, and additional libraries can be imported 
    # to be used in processing. The return value should be a Processed object, which is
    # what is returned by the process_images method.
    def run(self, p, checkbox):
        # TODO: get UI info through UI object angle, checkbox
        # proc = process_images(p)
        # TODO: add image edit process via Processed object proc
        print(checkbox)

        proc = process_images(p)
        return proc

















