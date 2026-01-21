# AI-Resume-Analyzer
基于 LLM 的智能简历诊断助手，支持 PDF 解析与多维度评估

AI 智能简历诊断助手，一款基于大模型驱动的自动化简历分析工具，专为校招求职者设计。

## 核心功能
- **PDF 自动解析**：利用 PyPDF2 实现非结构化文档的精准提取。 
- **智能诊断**：接入 DeepSeek/OpenAI 模型，从 HR 视角提供评分、优缺点分析及修改建议。 
- **鲁棒性设计**：内置完善的异常处理逻辑，支持流式响应，响应速度控制在 5s 内。 

## 技术栈
Python、Streamlit、DeepSeek API (LLM)、PyPDF2

##  快速启动
1. 安装依赖：`pip install -r requirements.txt`
2. 运行应用：`streamlit run app.py`
