from collections import Counter

# 등장 빈도 기준 정제 함수
def clean_by_freq(tokenized_words, cut_off_count):

    # Python의 Counter 모듈을 통해 단어의 빈도수 카운트하여 단어 집합 생성
    vocab = Counter(tokenized_words)

    # 빈도수가 cut_off_count 이하인 단어 set 추출
    uncommon_words = {key for key, value in vocab.items() if value <= cut_off_count}

    # uncommon_words에 포함되지 않는 단어 리스트 생성
    cleaned_words = [word for word in tokenized_words if word not in uncommon_words]

    return cleaned_words

