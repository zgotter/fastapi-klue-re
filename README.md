# FastAPI로 구현한 KLUE RE

## Install

```
python -m venv .venv
```

```
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

<br>

## Run

### fastapi

```
python -m app
```

### streamlit

```
streamlit run app/frontend.py
```

<br>

`http://localhost:8501`로 접속하면 화면을 확인할 수 있다.

<br>

## How to use

1. Entity 사이의 관계를 알고 싶은 문장을 선택한다.
2. Subject Entity 단어를 입력한다.
3. Object Entity 단어를 입력한다.
4. "관계 예측" 버튼을 클릭하여 두 entity 사이의 관계를 확인한다.