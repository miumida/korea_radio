# Korea Radio

![HAKC)][hakc-shield]
![HACS][hacs-shield]
![Version v1.4][version-shield]

<a href="https://www.buymeacoffee.com/miumida" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/white_img.png" alt="Buy Me A Coffee"></a>

Korea Radio 커스텀 컴포넌트 입니다.<br>
소나미님께서 작성하신 파이썬 소스를 컴포넌트화 시켰습니다.<br>
방송사에서 막으면 컴포넌트 수정이 불가하여, 지원이 안될 수도 있습니다.<br>
아쉽지만 MBC와 EBS 밖에 지원이 되지 않습니다<br>

<br>

## Version history
| Version | Date        | 내용              |
| :-----: | :---------: | ----------------------- |
| v1.0.0  | 2021.08.16  | First version  |

<br>

## Installation
### Manual
- HA 설치 경로 아래 custom_components에 korea_radio폴더 안의 전체 파일을 복사해줍니다.<br>
  `<config directory>/custom_components/korea_radio/`<br>
- configuration.yaml 파일에 설정을 추가합니다.<br>
- Home-Assistant 를 재시작합니다<br>
### HACS
- HACS > Integretions > 우측상단 메뉴 > Custom repositories 선택
- 'https://github.com/miumida/korea_radio' 주소 입력, Category에 'integration' 선택 후, 저장
- HACS > Integretions 메뉴 선택 후, korea_radio 검색하여 설치

<br>

## Usage
### Configuration(yaml)
- configuration.yaml 파일에 아래와 같이 설정을 추가합니다.
```yaml
korea_radio:
```
### Service Call
```yaml
service: korea_radio.play_radio
data:
  entity_id: media_player.mini
  channel: mbcfm4u
```

<br>

## 지원하는 라디오 방송
|구분|channel|
|-------|---------|
|EBS|EBS|
|MBC FM4U|mbcfm4u|
|MBC 표준FM|mbcfm|
|MBC allthat|allthat|

<br>

#### thanks to.
- 네이버 HomeAssistant 카페 | 소나미님

<br>

## 참고사이트
[1] 네이버 HomeAssistant 카페 | 소나미님의 [HA] HA => 구글 홈 미니로 라디오 재생 방법! final (<https://cafe.naver.com/koreassistant/5760>)<br>

[version-shield]: https://img.shields.io/badge/version-v1.0.0-orange.svg
[hakc-shield]: https://img.shields.io/badge/HAKC-Enjoy-blue.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Custom-red.svg
