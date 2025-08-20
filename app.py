import gradio as gr
from agents.buyer_agent import buyer_agent
from agents.seller_agent import seller_agent
from agents.renter_agent import renter_agent

# Registry
agents = {
    "BuyerAgent": buyer_agent,
    "SellerAgent": seller_agent,
    "RenterAgent": renter_agent,
}

# Functions for UI
def query_agent(agent: str, message: str):
    if agent in agents:
        return agents[agent](message)
    return "❌ Unknown agent"

def query_all(message: str):
    return {name: fn(message) for name, fn in agents.items()}

# Build UI
def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("## 🏡 RealEstateV1 - Multi-Agent Playground")

        with gr.Tab("Single Agent"):
            msg = gr.Textbox(label="Message")
            agent = gr.Dropdown(list(agents.keys()), label="Choose Agent")
            output = gr.Textbox(label="Agent Response")
            btn = gr.Button("Send")
            btn.click(fn=query_agent, inputs=[agent, msg], outputs=output)

        with gr.Tab("All Agents"):
            msg_all = gr.Textbox(label="Message for All Agents")
            outputs_all = gr.JSON(label="All Responses")
            btn_all = gr.Button("Broadcast")
            btn_all.click(fn=query_all, inputs=msg_all, outputs=outputs_all)

    return demo

if __name__ == "__main__":
    demo = build_ui()
    demo.launch(server_name="0.0.0.0", server_port=7860)
