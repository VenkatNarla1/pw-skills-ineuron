import gradio as gr

with gr.Blocks() as demo:
    gr.Label("ArtiFoto - AI image editor")
    with gr.Accordion("Upload image to edit"):
        with gr.Row():
            input_image=gr.Image()
            upload_button=gr.Button("UPLOAD")
    with gr.Tab("Automatic colour correction"):
        with gr.Row():
            # image_input = gr.Image()
            image_output1 = gr.Image()
    with gr.Tab("Image Sharpening"):
        with gr.Row():
            # image_input = gr.Image()
            image_output3 = gr.Image()
        show_button2 = gr.Button("Show")
    with gr.Tab("Object detection"):
        with gr.Row():
            # image_input = gr.Image()
            image_output2 = gr.Image()
        show_button1 = gr.Button("Show")
        # image_button = gr.Button("Show")
    upload_button.click(corrector,inputs=input_image,outputs=image_output1)
    show_button1.click(image_detect,inputs=input_image,outputs=image_output2)
    show_button2.click(sharpen,inputs=input_image,outputs=image_output3)

demo.launch(share=True)