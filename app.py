import streamlit as st
from datetime import date, timedelta
from models.predictor import predict
from utils.ai_advice import advice
from utils.chart import cycle_chart

st.set_page_config(page_title="LunaCare", page_icon="🌸", layout="wide")

st.markdown("""
<style>
body{background:#fff5fa;}
[data-testid="stMetric"]{
background:white;
padding:18px;
border-radius:18px;
box-shadow:0 5px 20px #eee;
}
</style>
""", unsafe_allow_html=True)

st.title("🌸 LunaCare")
st.caption("AI 智能女性健康周期管理系统")

a,b,c=st.columns(3)
a.metric("健康评分","92")
b.metric("预测可信度","91.6%")
c.metric("系统状态","正常")

st.divider()

st.header("📅 智能周期分析")
last=st.date_input("最近一次周期开始日期",date.today())
cycle=st.slider("平均周期",21,45,28)
pain=st.slider("疼痛程度",0,10,2)
mood=st.select_slider("今日情绪",["低落","一般","良好","开心"])

if st.button("✨ 生成分析报告"):
    result=predict(last,cycle)
    st.success("预计下一周期："+str(result))
    st.info(advice(pain,mood))

st.header("📊 周期趋势")
st.plotly_chart(cycle_chart(),use_container_width=True)

st.warning("本系统用于健康管理学习研究，不作为医疗诊断工具。")