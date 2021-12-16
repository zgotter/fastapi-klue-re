import pandas as pd
import streamlit as st
import requests
import json

st.set_page_config(layout="wide")

def main():
    st.title("KLUE RE Classification")

    sentence = st.selectbox(
        "문장 선택",
        [
            '〈Something〉는 조지 해리슨이 쓰고 비틀즈가 1969년 앨범 《Abbey Road》에 담은 노래다.',
            '호남이 기반인 바른미래당·대안신당·민주평화당이 우여곡절 끝에 합당해 민생당(가칭)으로 재탄생한다.',
            'K리그2에서 성적 1위를 달리고 있는 광주FC는 지난 26일 한국프로축구연맹으로부터 관중 유치 성과와 마케팅 성과를 인정받아 ‘풀 스타디움상’과 ‘플러스 스타디움상’을 수상했다.',
            '균일가 생활용품점 (주)아성다이소(대표 박정부)는 코로나19 바이러스로 어려움을 겪고 있는 대구광역시에 행복박스를 전달했다고 10일 밝혔다.',
            '1967년 프로 야구 드래프트 1순위로 요미우리 자이언츠에게 입단하면서 등번호는 8번으로 배정되었다.',
            ': 유엔, 유럽 의회, 북대서양 조약 기구 (NATO), 국제이주기구, 세계 보건 기구 (WHO), 지중해 연합, 이슬람 협력 기구, 유럽 안보 협력 기구, 국제 통화 기금, 세계무역기구 그리고 프랑코포니.',
            '그에 따라 나폴리와 계약을 연장한 마라도나는 1989년 팀을 UEFA컵 정상으로 인도했으며 이듬해에는 유럽 챔피언 AC 밀란을 상대로 승리를 거두고 다시 한 번 세리에A에서 정상에 등극했다.',
            '박용오(朴容旿, 1937년 4월 29일(음력 3월 19일)(음력 3월 19일) ~ 2009년 11월 4일)는 서울에서 태어난 대한민국의 기업인으로 두산그룹 회장, KBO 총재 등을 역임했다.',
            '중공군에게 온전히 대항할 수 없을 정도로 약해진 국민당은 타이베이로 수도를 옮기는 것을 결정해, 남아있는 중화민국군의 병력이나 국가, 개인의 재산등을 속속 타이완으로 옮기기 시작해, 12월에는 중앙 정부 기구도 모두 이전해 타이베이 시를 중화민국의 새로운 수도로 삼았다.',
            '특히 김동연 전 경제부총리를 비롯한 김두관 국회의원, 안규백 국회의원, 김종민 국회의원, 오제세 국회의원, 최운열 국회의원, 김정우 국회의원, 권칠승 국회의원, 맹성규 국회의원등 더불어민주당 국회의원 8명이 영상 축하 메세지를 보내 눈길을 끌었다.'
        ]
    )    

    st.write(sentence)

    subject_word = st.text_input("subject 단어 입력")
    subject_entity = None

    if subject_word not in sentence:
        st.error(f"{subject_word}(이)가 문장 내에 없습니다.")
    elif subject_word in sentence and subject_word != "":
        subject_entity = {
            "word": subject_word,
            "start_idx": sentence.find(subject_word),
            "end_idx": sentence.find(subject_word) + len(subject_word) - 1,
            "type": ""
        }
        st.success(f"subject : {subject_entity}")

    object_word = st.text_input("object 단어 입력")
    object_entity = None

    if object_word not in sentence:
        st.error(f"{object_word}(이)가 문장 내에 없습니다.")
    elif object_word in sentence and object_word != "":
        object_entity = {
            "word": object_word,
            "start_idx": sentence.find(object_word),
            "end_idx": sentence.find(object_word) + len(object_word) - 1,
            "type": ""
        }
        st.success(f"object : {object_entity}")

    data = None
    if sentence and subject_entity and object_entity:
        data = {
            "id": [0],
            "sentence": [sentence],
            "subject_entity": [subject_entity],
            "object_entity": [object_entity],
            "label": [100],
            "source": ["wikitree"]
        }

    if data is not None:
        if st.button("관계 예측"):
            st.write("예측중...")
            response = requests.post("http://localhost:8001/predict", data=json.dumps(data))
            relation = response.json()["relation"]
            st.info(f"관계: {relation}")

main()