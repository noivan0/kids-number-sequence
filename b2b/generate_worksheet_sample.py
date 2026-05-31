#!/usr/bin/env python3
"""
실제 사용 가능한 PDF 워크시트 샘플 생성기
주제: 10씩 더하고 빼기 (Phase 2-D 핵심 활동)
대상: 5~6세
"""

from fpdf import FPDF
import os

class WorksheetPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=12)
        font_path = "/mnt/d/kids-number-sequence/fonts/NanumGothic.ttf"
        self.add_font("Nanum", "", font_path)

    def draw_ten_frame(self, x, y, count, size=9):
        """간단한 10개 프레임 (시각화)"""
        self.set_draw_color(180, 180, 180)
        self.set_fill_color(255, 255, 255)
        for i in range(10):
            col = i % 5
            row = i // 5
            self.rect(x + col * (size+1.5), y + row * (size+1.5), size, size, "DF")
            if i < count:
                self.set_fill_color(16, 185, 129)
                self.rect(x + col * (size+1.5) + 1, y + row * (size+1.5) + 1, size-2, size-2, "F")
                self.set_fill_color(255, 255, 255)

    def draw_number_line(self, x, y, start, end, step, highlight=None):
        """간단한 수직선"""
        self.set_draw_color(100, 100, 100)
        self.line(x, y, x + 170, y)
        # ticks
        pos = 0
        for num in range(start, end+1, step):
            self.line(x + pos, y-2, x + pos, y+2)
            self.set_xy(x + pos - 6, y + 3)
            self.set_font("Nanum", "", 8)
            self.set_text_color(80, 80, 80)
            self.cell(12, 4, str(num), align="C")
            if highlight and num == highlight:
                self.set_fill_color(251, 191, 36)
                self.rect(x + pos - 5, y - 8, 10, 5, "F")
            pos += 170 / ((end - start) // step)

def create_worksheet():
    pdf = WorksheetPDF()
    
    # ========== PAGE 1 ==========
    pdf.add_page()
    
    # Header
    pdf.set_fill_color(16, 185, 129)
    pdf.rect(0, 0, 210, 22, "F")
    pdf.set_xy(12, 6)
    pdf.set_font("Nanum", "", 16)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, "🌟 10씩 더하고 빼기 놀이 (오프라인 활동지)", ln=True)
    pdf.set_xy(12, 14)
    pdf.set_font("Nanum", "", 9)
    pdf.cell(0, 5, "이름: ________________    날짜: __________    반: __________", ln=True)
    
    # Section 1: Warm-up
    y = 28
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 12)
    pdf.set_text_color(16, 185, 129)
    pdf.cell(0, 7, "1. 먼저 10개씩 세어볼까요?", ln=True)
    
    pdf.set_xy(12, y+8)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(185, 5, "아래 그림을 보고 10개씩 동그라미 쳐보세요. 10개가 몇 묶음인지 세어보고 숫자를 써보세요!")
    
    # Visual counting boxes (simple circles representation)
    y = 48
    pdf.set_xy(15, y)
    pdf.set_font("Nanum", "", 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, "예시:  ●●●●●  ●●●●●   = 10개  →  10", ln=True)
    
    examples = [
        ("18개", 18),
        ("27개", 27),
        ("32개", 32),
    ]
    box_y = y + 10
    for label, count in examples:
        pdf.set_xy(15, box_y)
        pdf.set_font("Nanum", "", 10)
        pdf.set_text_color(15, 23, 42)
        pdf.cell(25, 6, f"{label} : ", ln=False)
        # Draw simple dots representation
        pdf.set_xy(40, box_y)
        pdf.set_font("Nanum", "B", 11)
        pdf.set_text_color(16, 185, 129)
        pdf.cell(30, 6, "□ 10개 × ____ +  ○ ____개", ln=True)
        box_y += 9
    
    # Section 2: Main activity - Add 10
    y = 95
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 12)
    pdf.set_text_color(14, 165, 233)
    pdf.cell(0, 7, "2. 10씩 더해보기 (10을 단위로 생각하기)", ln=True)
    
    pdf.set_xy(12, y+8)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(185, 5, "시작 숫자에서 10씩 더해서 다음 칸을 채워보세요. 10을 한 덩어리로 생각하면 쉬워요!")
    
    # Table for adding 10
    y = 115
    pdf.set_font("Nanum", "B", 9)
    pdf.set_fill_color(224, 242, 255)
    headers = ["시작", "+10", "+10", "+10", "+10", "규칙 발견!"]
    col_width = 28
    pdf.set_xy(15, y)
    for h in headers:
        pdf.cell(col_width, 7, h, border=1, fill=True, align="C")
    pdf.ln()
    
    problems = [
        ["24", "___", "___", "___", "___", "10씩 더하면 ______"],
        ["37", "___", "___", "___", "___", "십의 자리가 ______"],
        ["52", "___", "___", "___", "___", "항상 ______의 배수"],
    ]
    pdf.set_font("Nanum", "", 10)
    pdf.set_text_color(15, 23, 42)
    for row in problems:
        pdf.set_x(15)
        for i, val in enumerate(row):
            pdf.cell(col_width, 8, val, border=1, align="C")
        pdf.ln()
    
    # Section 3: Subtract 10
    y = 155
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 12)
    pdf.set_text_color(244, 63, 94)
    pdf.cell(0, 7, "3. 10씩 빼보기 (거꾸로 생각하기)", ln=True)
    
    pdf.set_xy(12, y+8)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(185, 5, "이번엔 10씩 빼보세요. 10을 한 번에 빼면 십의 자리가 어떻게 변할까요?")
    
    y = 175
    pdf.set_font("Nanum", "B", 9)
    pdf.set_fill_color(255, 228, 230)
    headers2 = ["시작", "-10", "-10", "-10", "무엇이 변했나요?"]
    pdf.set_xy(15, y)
    for h in headers2:
        pdf.cell(33, 7, h, border=1, fill=True, align="C")
    pdf.ln()
    
    problems2 = [
        ["68", "___", "___", "___", "십의 자리가 ______"],
        ["81", "___", "___", "___", "십의 자리가 ______"],
    ]
    pdf.set_font("Nanum", "", 10)
    pdf.set_text_color(15, 23, 42)
    for row in problems2:
        pdf.set_x(15)
        for val in row:
            pdf.cell(33, 8, val, border=1, align="C")
        pdf.ln()
    
    # Section 4: Challenge
    y = 210
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 12)
    pdf.set_text_color(245, 158, 11)
    pdf.cell(0, 7, "4. 도전! 왕복 놀이 (더했다 뺐다)", ln=True)
    
    pdf.set_xy(12, y+8)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(185, 5, "시작 → 10 더하기 → 10 빼기 → 다시 10 더하기. 마지막 숫자는?")
    
    y = 228
    pdf.set_font("Nanum", "", 10)
    pdf.set_xy(15, y)
    pdf.cell(0, 6, "시작: 35   →   +10 = _____   →   -10 = _____   →   +10 = _____", ln=True)
    
    pdf.set_xy(15, y+10)
    pdf.set_font("Nanum", "B", 10)
    pdf.set_text_color(16, 185, 129)
    pdf.cell(0, 6, "★ 규칙: 10씩 더하고 빼면, 일의 자리는 절대 안 변해요! (항상 5로 끝남)", ln=True)
    
    # Footer
    pdf.set_xy(12, 265)
    pdf.set_font("Nanum", "", 8)
    pdf.set_text_color(148, 163, 184)
    pdf.cell(0, 5, "이 활동지는 '숫자 순서대로!' Phase 2-D와 함께 사용하면 효과가 더 좋습니다.", ln=True)
    pdf.cell(0, 5, "웹에서 플레이: https://noivan0.github.io/kids-number-sequence/   |   완전 무료", ln=True)
    
    # ========== PAGE 2: Teacher Guide ==========
    pdf.add_page()
    
    pdf.set_fill_color(245, 158, 11)
    pdf.rect(0, 0, 210, 18, "F")
    pdf.set_xy(12, 5)
    pdf.set_font("Nanum", "B", 14)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 8, "📋 선생님을 위한 활동 가이드 (Phase 2-D)", ln=True)
    
    y = 25
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 11)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 6, "이 워크시트의 교육적 의도", ln=True)
    
    pdf.set_xy(12, y+7)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(185, 5, 
        "이 활동은 아이들이 '10'을 단순한 숫자가 아니라 '크기 있는 단위'로 느끼도록 돕습니다. "
        "십의 자리가 변하는 경험을 통해 10의 특별함을 체득하게 됩니다.")
    
    y = 48
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 11)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 6, "수업 진행 팁 (15~20분)", ln=True)
    
    tips = [
        "1. 동전이나 블록 10개로 실제 '10 덩어리'를 만들어 보여주기",
        "2. 아이가 '십의 자리가 올라간다/내려간다'를 직접 말하게 하기",
        "3. '일의 자리는 왜 그대로일까?' 질문으로 규칙 발견 유도",
        "4. 잘한 아이는 '20씩 더하기'로 확장 도전 (보너스)",
        "5. 어려워하는 아이는 10개짜리 묶음만 먼저 세어보게 하기"
    ]
    pdf.set_xy(12, y+7)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    for tip in tips:
        pdf.set_x(15)
        pdf.multi_cell(180, 5.5, tip)
    
    y = 95
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 11)
    pdf.set_text_color(15, 23, 42)
    pdf.cell(0, 6, "관찰 포인트 (이 아이는 어떤 수준인가?)", ln=True)
    
    levels = [
        "● 상 : 10을 한 번에 처리하고, '십의 자리'라는 말을 스스로 사용",
        "● 중 : 10씩 더하고 빼는 계산은 가능하나, 왜 그런지 설명은 아직 어려움",
        "● 하 : 10개씩 세는 것 자체가 아직 어색함 → 1부터 10까지 세는 연습부터"
    ]
    pdf.set_xy(12, y+7)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    for lv in levels:
        pdf.set_x(15)
        pdf.multi_cell(180, 5.5, lv)
    
    y = 125
    pdf.set_xy(12, y)
    pdf.set_font("Nanum", "B", 11)
    pdf.set_text_color(16, 185, 129)
    pdf.cell(0, 6, "웹 게임과 연계하면 더 강력합니다", ln=True)
    
    pdf.set_xy(12, y+7)
    pdf.set_font("Nanum", "", 9.5)
    pdf.set_text_color(51, 65, 85)
    pdf.multi_cell(185, 5, 
        "이 워크시트를 한 후 '숫자 순서대로!' Phase 2-D '10씩 더하고 빼기' 트랙을 해보세요. "
        "실제 조작 경험(웹) + 종이 활동(오프라인)이 서로를 강화합니다. "
        "아이들이 '아! 이게 그거구나!' 하면서 연결 짓는 순간을 놓치지 마세요.")
    
    # Contact box
    pdf.set_fill_color(240, 253, 244)
    pdf.rect(12, 155, 186, 28, "DF")
    pdf.set_xy(15, 158)
    pdf.set_font("Nanum", "B", 10)
    pdf.set_text_color(16, 185, 129)
    pdf.cell(0, 6, "더 많은 자료가 필요하신가요?", ln=True)
    pdf.set_xy(15, 164)
    pdf.set_font("Nanum", "", 9)
    pdf.set_text_color(51, 65, 85)
    pdf.cell(0, 5, "• 전체 Phase 워크시트 세트 (PDF) 요청 가능", ln=True)
    pdf.cell(0, 5, "• 학급 전체 리포트 자동 생성 기능 (B2B 도입 시 제공)", ln=True)
    pdf.cell(0, 5, "• 무료 2주 체험 문의: noivan000@gmail.com", ln=True)
    
    pdf.set_xy(12, 190)
    pdf.set_font("Nanum", "B", 9)
    pdf.set_text_color(100, 116, 139)
    pdf.cell(0, 5, "제작: 숫자 순서대로! | https://noivan0.github.io/kids-number-sequence/ | Phase 1~4 완전 무료", align="C")
    
    output_path = "/mnt/d/kids-number-sequence/b2b/워크시트_샘플_10씩더하고빼기_v1.pdf"
    pdf.output(output_path)
    print(f"✅ 워크시트 샘플 생성 완료: {output_path}")
    return output_path

if __name__ == "__main__":
    create_worksheet()