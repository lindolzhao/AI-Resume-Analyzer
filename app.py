import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI

# 1. 设置页面标题
st.set_page_config(page_title="智能简历分析助手", page_icon="📄")
st.title("📄 AI 智能简历诊断助手")

# 2. 侧边栏：输入 API Key (不用把 Key 写死在代码里，安全)
api_key = st.sidebar.text_input("请输入 DeepSeek/OpenAI API Key", type="password")

# 3. 文件上传功能
uploaded_file = st.file_uploader("请上传你的 PDF 简历", type="pdf")

# 4. 核心逻辑：当用户上传文件且点击分析按钮
if uploaded_file is not None and api_key:
    # --- 读取 PDF ---
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.write("✅ 简历解析成功！正在思考中...")

    # --- 调用大模型 (这里以 DeepSeek/OpenAI 格式为例) ---
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")  # 如果用 OpenAI 就不需要 base_url

    # 构造提示词 (Prompt) - 这是最关键的地方！
    prompt = f"""
    你是一位资深的 HR 和技术面试官。请阅读以下简历内容，并给出分析：
    1. 【评分】：给这份简历打分（0-100分）。
    2. 【优点】：找出 3 个亮点。
    3. 【致命伤】：找出 2 个需要改进的弱点。
    4. 【修改建议】：给出具体的修改话术。

    简历内容：
    {text}
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",  # 或者 gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        # --- 展示结果 ---
        result = response.choices[0].message.content
        st.markdown("### 🤖 AI 分析报告")
        st.markdown(result)

    except Exception as e:
        st.error(f"调用 API 出错: {e}")

elif not api_key:
    st.warning("👈 请先在左侧输入 API Key")