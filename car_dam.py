import streamlit as st
from ultralytics import YOLO
from PIL import Image

# 1. Setup the Page - Professional Branding
st.set_page_config(page_title="Auto-Insure AI", page_icon="🚗", layout="centered")

st.title("🚗 Auto-Insure: Smart Damage Detection")
st.markdown("""
    **AI-Powered Vehicle Inspection System** Upload a vehicle image to perform a real-time diagnostic scan. 
    The system identifies anomalies and calculates repair priority scores.
""")

# 2. Load the Model (YOLOv8)
@st.cache_resource
def load_model():
    # Returns the model object; cached to prevent reloading on every click
    return YOLO('yolov8n.pt') 

model = load_model()

# 3. Sidebar for Project Metadata (Looks great on Resume)
with st.sidebar:
    st.header("System Status")
    st.success("Model: YOLOv8 Nano")
    st.info("Environment: Production V1.0")
    st.divider()
    st.write("Developed for automated insurance triaging.")

# 4. Upload UI
uploaded_file = st.file_uploader("Choose a car image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    
    # Run the AI Detection with a set confidence threshold
    results = model.predict(source=img, conf=0.30)
    
    # UI Layout: Two columns for Image and Analysis
    col1, col2 = st.columns([2, 1])
    
    with col1:
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="Visual AI Analysis", use_container_width=True)
    
    with col2:
        # Extract Data Logic
        boxes = results[0].boxes
        damage_count = len(boxes)
        # Calculate average confidence of detections
        avg_conf = sum(boxes.conf.tolist()) / damage_count if damage_count > 0 else 0
        
        st.subheader("Metrics")
        st.metric("Anomalies Found", damage_count)
        st.metric("Confidence Score", f"{avg_conf:.1%}")

    # 5. Advanced Severity Logic
    st.divider()
    if damage_count > 0:
        # If confidence is high or count is high, it's a priority case
        if damage_count > 3 or avg_conf > 0.85:
            st.error("### Priority: HIGH (Major Damage)")
            st.write("Immediate manual inspection and adjuster assignment required.")
        else:
            st.warning("### Priority: LOW (Minor Surface Issues)")
            st.write("Standard repair track; cosmetic damage detected.")
            
        # 6. Detailed Data Report (The 'Pro' touch)
        with st.expander("See Raw Diagnostic Data"):
            for i, box in enumerate(boxes):
                label = model.names[int(box.cls)]
                st.write(f"Detection {i+1}: **{label.capitalize()}** | Confidence: {box.conf.item():.2f}")
    else:
        st.success("### Status: NO DAMAGE DETECTED")
        st.write("The vehicle appears to be in optimal condition.")

else:
    st.info("Please upload an image to begin the automated diagnostic process.")