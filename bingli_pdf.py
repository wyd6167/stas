import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PathologyReport:
    def __init__(self, patient_info, diagnosis_description, diagnosis_result, visualizations):
        self.patient_info = patient_info
        self.diagnosis_description = diagnosis_description
        self.diagnosis_result = diagnosis_result
        self.visualizations = visualizations

    def generate_report(self, pdf_filename):
        # 创建PDF文档
        pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

        # 写入患者信息
        pdf_canvas.drawString(100, 750, f"姓名: {self.patient_info['姓名']}")
        pdf_canvas.drawString(100, 735, f"性别: {self.patient_info['性别']}")
        pdf_canvas.drawString(100, 720, f"送检日期: {self.patient_info['送检日期']}")

        # 写入诊断描述
        pdf_canvas.drawString(100, 680, f"标本类型: {self.diagnosis_description['标本类型']}")
        pdf_canvas.drawString(100, 665, f"样本质量: {self.diagnosis_description['样本质量']}")

        # 写入诊断结果
        pdf_canvas.drawString(100, 625, f"诊断结果: {self.diagnosis_result}")

        # 插入图表
        for i, visualization in enumerate(self.visualizations, 1):
            pdf_canvas.drawInlineImage(visualization, 100, 550 - i * 150, width=300, height=200)

        # 保存PDF文档
        pdf_canvas.save()

        print(f"报告已生成，保存为 {pdf_filename}")

# 示例数据
patient_info = {'姓名': '张三', '性别': '男', '送检日期': '2024-01-26'}
diagnosis_description = {'标本类型': '肺组织', '样本质量': '良好'}
diagnosis_result = 'STAS阳性'
visualizations = [r'F:\python\mypy1\stas_system\stas_system\result\1637460-G.png', r'F:\python\mypy1\stas_system\stas_system\result\1637460-G.png']  # 图像路径

# 创建报告对象并生成报告
pdf_filename = 'pathology_report.pdf'
report = PathologyReport(patient_info, diagnosis_description, diagnosis_result, visualizations)
report.generate_report(pdf_filename)
