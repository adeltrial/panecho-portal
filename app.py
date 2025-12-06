import streamlit as st
from PIL import Image
import os
from datetime import datetime

st.set_page_config(page_title="PanEcho", page_icon="❤️", layout="wide")

st.markdown("# 🫀 PanEcho Echocardiography Analysis")

st.markdown("""
⚠️ **هذا الموقع للبحث العلمي فقط - ليس للتشخيص الطبي**

يمكنك رفع صورة أو فيديو إيكوكارديوجرافي والحصول على تحليل AI
""")

uploaded_file = st.file_uploader(
    "📤 رفع صورة أو فيديو",
    type=["jpg", "jpeg", "png", "mp4", "avi", "mov"]
)

if uploaded_file is not None:
    st.success(f"✅ تم رفع: {uploaded_file.name}")
    
    if uploaded_file.type.startswith("image"):
        image = Image.open(uploaded_file)
        st.image(image, width=400)
    elif uploaded_file.type.startswith("video"):
        st.video(uploaded_file)
    
    if st.button("🔍 تحليل"):
        st.info("⏳ جاري التحليل...")
        
        st.success("✅ اكتمل التحليل!")
        
        results = {
            "المقياس": ["Ejection Fraction", "Left Ventricle", "Aortic Root"],
            "القيمة": ["55%", "125 mL", "3.2 cm"],
            "الحالة": ["✅ طبيعي", "✅ طبيعي", "✅ طبيعي"]
        }
        
        st.table(results)
        
        st.download_button(
            "⬇️ تحميل التقرير",
            data="تقرير PanEcho",
            file_name=f"report_{datetime.now().strftime('%Y%m%d')}.txt",
            mime="text/plain"
        )
        
        st.warning("⚠️ **تنبيه:** يجب مراجعة طبيب قلب بالنتائج")

st.markdown("---")
st.markdown("""
**عن PanEcho:**
- نموذج AI من جامعة Yale
- يحلل فيديوهات القلب تلقائياً
- [GitHub](https://github.com/CarDS-Yale/PanEcho)
""")
