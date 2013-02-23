# Korea Assembly Officials Property

This repo contains South Korean 19th Assembly Officials' property data in usable formats.

The following formats are available:

- csv
- json (In preparation)

## Development Notes

	data/
	└── 20120530/
    	├── 0_raw.pdf
    	├── 1_extracted.xlsx
	    ├── 2_converted.csv
    	├── 3_sanitized.csv
	    └── 4_aligned.csv

### 데이터셋

- 데이터명: [제 19대 국회 신규등록 국회의원 재산등록사항 (`0_raw.pdf`)](http://ebook.assembly.go.kr/HLOpenPDF.jsp?file=general72973655.pdf&keyword=78%C8%A3&system=GENERALPUB)
- 원본 출처 시스템: [국회발간자료](http://ebook.assembly.go.kr/)
- 신규등록: 18대엔 국회의원이 아니었으나 19대에는 선출된 의원 (초선과는 다름) 

### 활용 목적
- 국회의원 재산 현황을 지속적으로 기록하여 임의의 사안이 있을 때 재산 변동의 원인을 확인한다.

### 데이터 품질 및 정제 필요 항목
- pdf 형태로 공개되어 있어 타 포멧(엑셀, csv, json 등)으로 기계적으로 변환 불가

### 개선 방법 및 도구
1. nitro를 이용해 pdf를 엑셀 형태로 변환. 하지만 한 항목이 여러 줄에 걸쳐 있거나 열(column)의 수가 다른 등, 구조화되어있지 않음.
2. xls 파일을 csv로 변환
3. python script를 작성해 한 항목이 한 줄을 나타내도록 정제
4. python script를 작성해 같은 속성은 같은 열에 위치하도록 구조화. (일반적인 엑셀이나 csv)

### 외부 데이터 수집 및 연계
- 없음

## Contributors
- <a href="mailto:eunho.cha@gmail.com">Eunho Cha</a>, <a href="mailto:hjkwon@newstapa.org">Hyejin Kwon</a>, <a href="mailto:soulabe@newstapa.org">Yoonwon Choi</a>, <a href="mailto:lucypark@popong.com">Lucy Park</a>, <a href="mailto:steel@popong.com">Cheol Kang</a>, <a href="mailto:2424wlsgur@naver.com">Seongwook Choi</a>
- 2013 Open Data Day, <a href="http://www.facebook.com/OKFNKorea">OKFnKorea</a>

## Copyright and License
This data is made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/
