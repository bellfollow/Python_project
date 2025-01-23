class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def __repr__(self):
        return self.text
    #자꾸 객체 주소가 반환되서 찾아보니 __repr__가 빠져있었음 
    #Question 클래스에 __str__ 또는 __repr__ 메서드가 정의되어 있지 않으므로, print나 f-string에서 해당 인스턴스를 출력할 때 객체의 메모리 주소가 반환됩니다.