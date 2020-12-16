from sepChunk import divsen
from mkEumjul import mo


#은, 는, 이, 가, 을, 를
class decideJosa:
    noundata = [
        '사회', '불만세력', '가운데', '학생', '불안정', '미국', '흑인', '절망감', '생활여건', '학생신분',
        '대학', '고등교육기관', '모순', '남녀', '특권층', '위험', '무책임', '기술사회', '실험실', '청년층',
        '요인', '사회적소외', '소외', '세계', '격리', '집단생활', '현대사회', '사회체제', '공동체', '비판',
        '기계', '소멸', '대상', '저항', '아침', '화장실', '엄마', '잔소리', '강아지', '불',
        '식사', '시간', '밥', '말썽', '숟가락', '경례', '영화배우', '이야기', '오빠', '고모',
        '늦둥이', '친척', '청계천', '손잡이', '내리막길', '풍물', '만국기', '행사장', '한국인', '도사',
        '어둠', '하늘', '북극성', '별자리', '길잡이', '봄', '밤하늘', '직녀성', '견우성', '백조자리',
        '북두칠성', '밝기', '삼각형', '페가수스', '안드로메다', '가장', '케페우스', '전설', '그림책', '결혼',
        '거문고', '플루토', '아내', '체험관', '천막', '꿀밤', '머리', '봉', '이해', '실수',
        '태양', '행성', '반말', '천동설', '피조물', '종교', '혁명', '프랑스', '지동설', '코페르니쿠스',
    ]
    def __init__(self, l_noun = noundata):
        self.l_noun = l_noun
        self.l_jo = []
    def EunNeun(self):
        for n in self.l_noun:
            if list(divsen(n))[-1] in mo:
                self.l_jo.append('는')
            else:
                self.l_jo.append('은')
        return(self.l_jo)
    def IGa(self):
        for n in self.l_noun:
            if list(divsen(n))[-1] in mo:
                self.l_jo.append('가')
            else:
                self.l_jo.append('이')
        return (self.l_jo)
    def EulRul(self):
        for n in self.l_noun:
            if list(divsen(n))[-1] in mo:
                self.l_jo.append('를')
            else:
                self.l_jo.append('을')
        return (self.l_jo)
