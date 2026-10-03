"""
날씨 리포트 프로그램 (Open-Meteo API 사용)
- 사용자에게 지역을 입력받음 (기본값: 천안)
- 오늘, 내일, 모레까지 3 일간의 날씨를 오전 6 시, 오후 3 시 기준으로 표시
- Open-Meteo API 사용 (인증키 불필요, 무료)
"""

from typing import Optional

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

DEFAULT_REGION = "천안"
FORECAST_DAYS = 3
TARGET_HOURS = (6, 15)  # 오전 6 시, 오후 3 시
DAY_LABELS = ("오늘", "내일", "모레")
TIMEOUT = 10


def main() -> None:
    print("🌤️ 날씨 예보 프로그램 (Open-Meteo API)")
    print("-" * 50)
    print(f"오전 6 시, 오후 3 시 기준으로 {FORECAST_DAYS} 일간 날씨를 제공합니다.")
    print("-" * 50)
    print()

    region = input(f"날씨를 확인할 지역을 입력하세요 (기본값: {DEFAULT_REGION}): ").strip()
    if not region:
        region = DEFAULT_REGION

    print(f"📍 {region} 의 날씨 정보를 가져옵니다... (구현 예정)")


if __name__ == "__main__":
    main()
