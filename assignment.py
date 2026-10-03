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
REGION_SUFFIXES = ("특별시", "광역시", "특별자치시", "시", "군")
FORECAST_DAYS = 3
TARGET_HOURS = (6, 15)  # 오전 6 시, 오후 3 시
DAY_LABELS = ("오늘", "내일", "모레")
TIMEOUT = 10


def get_coordinates(region: str) -> Optional[dict]:
    """지역 이름으로 위도/경도를 조회한다. 찾지 못하면 None 을 반환한다."""
    # Open-Meteo 는 '서울', '천안' 같은 짧은 이름으로는 엉뚱한 곳을 찾기 때문에
    # '서울특별시', '천안시' 처럼 행정구역 이름을 붙여서 먼저 검색한다.
    candidates = [region + suffix for suffix in REGION_SUFFIXES] + [region]
    for name in candidates:
        try:
            response = requests.get(
                GEOCODING_URL,
                params={"name": name, "count": 5, "language": "ko",
                        "countryCode": "KR", "format": "json"},
                timeout=TIMEOUT,
            )
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ 지역 검색 중 오류가 발생했습니다: {e}")
            return None

        for place in response.json().get("results", []):
            if place["name"] == name:
                return {
                    "name": region,
                    "latitude": place["latitude"],
                    "longitude": place["longitude"],
                }
    return None


def main() -> None:
    print("🌤️ 날씨 예보 프로그램 (Open-Meteo API)")
    print("-" * 50)
    print(f"오전 6 시, 오후 3 시 기준으로 {FORECAST_DAYS} 일간 날씨를 제공합니다.")
    print("-" * 50)
    print()

    region = input(f"날씨를 확인할 지역을 입력하세요 (기본값: {DEFAULT_REGION}): ").strip()
    if not region:
        region = DEFAULT_REGION

    location = get_coordinates(region)
    if location is None:
        print(f"❌ '{region}' 지역을 찾을 수 없습니다.")
        return

    print()
    print(f"📍 {region} (위도: {location['latitude']:.4f}, 경도: {location['longitude']:.4f}) "
          f"의 날씨 정보를 가져옵니다...")
    # TODO: 날씨 API 연동


if __name__ == "__main__":
    main()
