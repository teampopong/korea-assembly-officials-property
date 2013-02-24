# Korea Assembly Officials Property

This repo contains South Korean 19th Assembly Officials' property data in usable formats.

## Data description

### 원본 데이터
- 원본 데이터 출처: [국회발간자료](http://ebook.assembly.go.kr/)
- 원본 데이터 이름: [제 19대 국회 신규등록 국회의원 재산등록사항](http://ebook.assembly.go.kr/HLOpenPDF.jsp?file=general72973655.pdf&keyword=78%C8%A3&system=GENERALPUB)
	- 신규등록 국회의원 **183명**을 대상으로 한 조사 자료.
	- 이 데이터는 "국회의원 재산 현황을 지속적으로 기록하여 임의의 사안이 있을 때 재산 변동의 원인을 확인"하기 위한 것으로, 정원 300명 전원에 대한 데이터가 아님.
	- 이 데이터는 pdf 형태로 공개되어 있어 기계적 접근이 어려움.

> 용어정리
> - **신규등록 국회의원**: 18대에는 국회의원이 아니었으나 19대에는 선출된 의원. 17대에 임용되고 18대에 임용되지 않고 19대에 재임용된 경우도 포함. '초선 국회의원'과는 다른 개념. (총 183명, 전체 정원의 61%)
> - **초선 국회의원**: 제19대 국회가 첫 당선인 의원. (총 148명, 전체 정원의 약 49.3%)

### 가공된 데이터

The following formats are available:

- [csv](https://github.com/teampopong/korea-assembly-officials-property/blob/master/data/20120530/4_aligned.csv)


## Development Notes

	data/
	└── 20120530/
    	├── 0_raw.pdf
    	├── 1_extracted.xlsx
	    ├── 2_converted.csv
    	├── 3_sanitized.csv
	    └── 4_aligned.csv

### 개선 방법 및 도구
1. `0_raw.pdf`>`1_extracted.xlsx`: [nitro](http://www.nitropdf.com/)를 이용해 pdf를 엑셀 형태로 변환함.
	- 변환 후에도  한 항목이 여러 줄에 걸쳐 있거나 열(column)의 수가 다른 등, 구조화되어있지 않음.
2. `1_extracted.xlsx`>`2_converted.csv`: xls 파일을 csv로 변환
3. `2_converted.csv`>`3_sanitized.csv`: python script를 작성해 한 항목이 한 줄을 나타내도록 정제
4. `3_sanitized.csv`>`4_aligned.csv`: [python script](https://github.com/teampopong/korea-assembly-officials-property/blob/master/align.py)를 작성해 같은 속성은 같은 열에 위치하도록 구조화. (일반적인 엑셀이나 csv)


## Contributors
- <a href="mailto:eunho.cha@gmail.com">Eunho Cha</a>, <a href="mailto:hjkwon@newstapa.org">Hyejin Kwon</a>, <a href="mailto:soulabe@newstapa.org">Yoonwon Choi</a>, <a href="mailto:lucypark@popong.com">Lucy Park</a>, <a href="mailto:steel@popong.com">Cheol Kang</a>, <a href="mailto:2424wlsgur@naver.com">Seongwook Choi</a>
- 2013 Open Data Day, <a href="http://www.facebook.com/OKFNKorea">OKFnKorea</a>

## Copyright and License
This data is made available under the Public Domain Dedication and License v1.0 whose full text can be found at: http://www.opendatacommons.org/licenses/pddl/1.0/
