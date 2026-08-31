import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

# .env 파일에서 OPENAI_API_KEY를 불러옵니다.
load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    symptom = data.get("symptom", "").strip()
    condition = data.get("condition", "").strip()

    # 이상 현상 입력 확인
    if not symptom:
        return jsonify({
            "error": "분석할 이상 현상을 입력해주세요."
        }), 400

    prompt = f"""
당신은 산업 설비 상태를 돕는 AI 분석 보조자입니다.

사용자가 입력한 정보를 바탕으로 다음 형식으로 한국어 답변을 작성하세요.

1. 예상 원인
2. 점검 항목
3. 권장 조치
4. 안전 주의사항

중요:
- 확정 진단처럼 말하지 말고, 가능성 또는 추정으로 표현하세요.
- 위험한 설비 작업은 반드시 전문가와 안전 절차를 따르도록 안내하세요.
- 간결하고 이해하기 쉽게 작성하세요.

이상 현상:
{symptom}

발생 조건:
{condition if condition else "입력되지 않음"}
"""

    try:
        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        return jsonify({
            "result": response.output_text
        })

    except Exception as error:
        print(error)

        return jsonify({
            "error": "AI 분석 중 오류가 발생했습니다. API 키와 인터넷 연결을 확인해주세요."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)