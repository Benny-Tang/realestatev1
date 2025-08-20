import gradio as gr
from agents.buyer_agent import BuyerAgent
from agents.seller_agent import SellerAgent
from agents.renter_agent import RenterAgent

# Initialize agents
buyer_agent = BuyerAgent()
seller_agent = SellerAgent()
renter_agent = RenterAgent()

agents = {
    "BuyerAgent": buyer_agent,
    "SellerAgent": seller_agent,
    "RenterAgent": renter_agent,
}

# --- Gradio functions ---
def query_agent(agent_name: str, message: str):
    if agent_name in agents:
        return agents[agent_name].run(message)
    return "❌ Unknown agent"

def query_all(message: str):
    return {name: agent.run(message) for name, agent in agents.items()}

# --- Build UI ---
def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 🏡 RealEstateV1 - Multi-Agent Playground")

        with gr.Tab("Single Agent"):
            msg = gr.Textbox(label="Message")
            agent = gr.Dropdown(list(agents.keys()), label="Choose Agent")
            output = gr.Textbox(label="Response")
            btn = gr.Button("Run")
            btn.click(fn=query_agent, inputs=[agent, msg], outputs=output)

        with gr.Tab("All Agents"):
            msg_all = gr.Textbox(label="Message for All Agents")
            outputs_all = gr.JSON(label="All Responses")
            btn_all = gr.Button("Run All")
            btn_all.click(fn=query_all, inputs=msg_all, outputs=outputs_all)

    return demo

# --- Run app ---
if __name__ == "__main__":
    demo = build_ui()
    demo.launch()
