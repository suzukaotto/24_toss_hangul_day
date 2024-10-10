# 토스 한글날 이벤트 매크로
## How to use
사용하기 전, 컴퓨터에서 실시간으로 핸드폰 화면을 불러오세요.<br>
윈도우에서 내 휴대폰과 연결을 사용해보세요.<br>
맥을 위한 프로그램은 아니에요..<br><br>

핸드폰 화면을 잘 불러왔다면, 코드에서 캡쳐될 구역을 설정해야합니다.<br>
DISPLAY_RIGHT_TOP = 캡쳐될 좌상단 좌표(x, y)<br>
DISPLAY_LEFT_BOTTOM = 캡쳐될 우하단 좌표(x, y)<br>
설정 후, 캡쳐가 아래와 같이 되어야 합니다.<br>
![올바른캡쳐](https://raw.githubusercontent.com/suzukaotto/24_toss_hangul_event/refs/heads/master/region_capture.png)<br><br>

메뉴 선택은 메뉴 명에 해당하는 숫자를 입력하면 됩니다.<br><br>

Config SPLITE_LEVEL 메뉴로 격자 개수를 설정할 수 있습니다.<br>
SPLIT_LEVEL이 2면 2x2, 3이면 3x3...<br>
격자를 설정하고 2번 메뉴를 누르면 됩니다.<br><br>

설정 후 Run 메뉴를 실행하면 됩니다.<br>
