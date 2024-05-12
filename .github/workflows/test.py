name: test.py

on:
  push:
    branches:
      - main  # 원하는 브랜치를 여기에 지정할 수 있습니다.

jobs:
  build:

    runs-on: ubuntu-latest  # 원하는 운영체제를 선택할 수 있습니다.

    steps:
    - uses: actions/checkout@v2  # 저장소의 코드를 체크아웃합니다.

    - name: Install dependencies  # 필요한 의존성을 설치합니다.
      run: npm install

    - name: Run tests  # 테스트를 실행합니다.
      run: npm test

