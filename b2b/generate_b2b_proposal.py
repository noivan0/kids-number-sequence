#!/usr/bin/env python3
"""
B2B 1-Page Proposal PDF Generator
숫자 순서대로! - 유치원/어린이집 대상 제안서
"""

from fpdf import FPDF
import os

class B2BProposalPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        # Korean font
        font_path = "/mnt/d/kids-number-sequence/fonts/NanumGothic.ttf"
        self.add_font("Nanum", "", font_path)
        self.add_font("Nanum", "B", font_path)  # Use same for bold (simplified)

    def header_section(self):
        # Top accent bar
        self.set_fill_color(16, 185, 129)  # emerald-600
        self.rect(0, 0, 210, 8, "F")

        # Logo + Title
        self.set_font("Nanum", "B", 22)
        self.set_text_color(16, 185, 129)
        self.set_xy(15, 15)
        self.cell(0, 10, "🌟 숫자 순서대로!", ln=True)

        self.set_font("Nanum", "", 11)
        self.set_text_color(100, 116, 139)
        self.set_xy(15, 25)
        self.cell(0, 6, "3~7세 아이를 위한 수 개념 규칙 발견 게임 | 완전 무료 체험 제공", ln=True)

    def section_title(self, title, y):
        self.set_xy(15, y)
        self.set_font("Nanum", "B", 13)
        self.set_text_color(15, 23, 42)
        self.cell(0, 8, title, ln=True)
        # underline
        self.set_draw_color(16, 185, 129)
        self.line(15, y + 8, 195, y + 8)

    def body_text(self, text, y, font_size=10.5):
        self.set_xy(15, y)
        self.set_font("Nanum", "", font_size)
        self.set_text_color(51, 65, 85)
        self.multi_cell(180, 5.5, text)

    def bullet(self, items, y):
        self.set_xy(15, y)
        self.set_font("Nanum", "", 10)
        self.set_text_color(51, 65, 85)
        for item in items:
            self.set_x(18)
            self.cell(0, 6, "•  " + item, ln=True)

    def highlight_box(self, title, content, y, color=(16, 185, 129)):
        self.set_fill_color(*color)
        self.set_draw_color(*color)
        self.rect(15, y, 180, 22, "DF")
        
        self.set_xy(18, y + 2)
        self.set_font("Nanum", "B", 11)
        self.set_text_color(255, 255, 255)
        self.cell(0, 6, title, ln=True)
        
        self.set_xy(18, y + 9)
        self.set_font("Nanum", "", 9.5)
        self.multi_cell(174, 5, content)

    def pricing_table(self, y):
        self.set_xy(15, y)
        self.set_font("Nanum", "B", 10)
        self.set_text_color(15, 23, 42)
        
        # Table header
        self.set_fill_color(240, 253, 244)  # light emerald
        self.cell(90, 8, "  구분", border=1, fill=True)
        self.cell(45, 8, "  가격 (월)", border=1, fill=True, align="C")
        self.cell(45, 8, "  비고", border=1, fill=True, align="C", ln=True)
        
        self.set_font("Nanum", "", 9.5)
        self.set_text_color(51, 65, 85)
        
        rows = [
            ("유치원 1반 (최대 25명)", "15,000원", "교사용 대시보드 포함"),
            ("어린이집 1개 학급", "15,000원", "학부모 리포트 공유 기능"),
            ("3반 이상 기관", "협의 (할인)", "전체 데이터 분석 + 맞춤 자료"),
        ]
        for label, price, note in rows:
            self.set_x(15)
            self.cell(90, 7, "  " + label, border=1)
            self.cell(45, 7, "  " + price, border=1, align="C")
            self.cell(45, 7, "  " + note, border=1, align="C", ln=True)

    def footer_section(self):
        y = 260
        self.set_xy(15, y)
        self.set_font("Nanum", "B", 10)
        self.set_text_color(16, 185, 129)
        self.cell(0, 6, "지금 바로 무료 체험을 시작하세요", ln=True)

        self.set_xy(15, y + 7)
        self.set_font("Nanum", "", 9)
        self.set_text_color(100, 116, 139)
        self.cell(0, 5, "데모 사이트: https://noivan0.github.io/kids-number-sequence/", ln=True)
        self.cell(0, 5, "문의: noivan000@gmail.com  |  30분 무료 시연 방문 가능 (서울/경기 우선)", ln=True)

        # Bottom bar
        self.set_fill_color(16, 185, 129)
        self.rect(0, 285, 210, 12, "F")
        self.set_xy(15, 287)
        self.set_font("Nanum", "B", 8)
        self.set_text_color(255, 255, 255)
        self.cell(0, 5, "연구 기반 · 광고 제로 · 부모가 실제로 확인할 수 있는 수 개념 교육 도구", align="C")

def create_proposal():
    pdf = B2BProposalPDF()
    
    # Header
    pdf.header_section()
    
    # Problem
    pdf.section_title("1. 현장 교육자분들이 느끼는 어려움", 38)
    pdf.bullet([
        "아이들마다 수 개념 수준 차이가 너무 커서 개별 지도가 어렵습니다.",
        "부모님께 '집에서 어떻게 도와주면 좋을까요?'라고 물을 때 구체적인 자료가 없습니다.",
        "기존 앱들은 광고가 많거나, '그냥 게임'처럼 느껴져 교육적 효과를 설명하기 어렵습니다."
    ], 47)
    
    # Solution
    pdf.section_title("2. 숫자 순서대로! 가 제공하는 해결책", 72)
    pdf.body_text(
        "아이 스스로 '규칙을 발견'하도록 설계된 교육 게임입니다. "
        "1씩, 2씩, 5씩, 10씩, 100씩… 아이가 직접 패턴을 찾아가며 10의 자리와 큰 수의 크기 감각을 체득합니다. "
        "Phase 1~4까지 총 22개 트랙이 모두 무료로 제공됩니다.", 80)
    
    # Benefits boxes
    pdf.section_title("3. 도입 시 기대 효과", 98)
    pdf.highlight_box(
        "아이에게", 
        "지루한 반복이 아닌 '스스로 발견하는 재미'. 20분 플레이로도 수 개념이 눈에 띄게 향상됩니다.",
        106, color=(16, 185, 129)
    )
    pdf.highlight_box(
        "선생님에게", 
        "아이별 진행 상황을 한눈에 파악. 학부모 상담 시 객관적인 자료로 활용 가능합니다.",
        130, color=(14, 165, 233)
    )
    pdf.highlight_box(
        "학부모에게", 
        "광고 없는 깨끗한 환경 + 구체적인 학습 리포트로 '우리 아이가 잘하고 있나?' 불안을 해소합니다.",
        154, color=(245, 158, 11)
    )
    
    # How it works
    pdf.section_title("4. 도입 절차 (매우 간단합니다)", 178)
    pdf.bullet([
        "1단계: 30분 무료 시연 (원하시는 시간에 방문 또는 온라인)",
        "2단계: 2주간 무료 체험 (1개 반 전체 사용 가능)",
        "3단계: 체험 후 피드백 → 정식 도입 결정",
        "4단계: 간단한 계약 후 바로 사용 시작"
    ], 186)
    
    # Pricing
    pdf.section_title("5. B2B 도입 비용 (2026년 기준)", 208)
    pdf.pricing_table(216)
    
    # CTA
    pdf.footer_section()
    
    # Save
    output_path = "/mnt/d/kids-number-sequence/b2b/B2B_제안서_숫자순서대로_v1.pdf"
    pdf.output(output_path)
    print(f"✅ B2B 제안서 생성 완료: {output_path}")
    return output_path

if __name__ == "__main__":
    create_proposal()