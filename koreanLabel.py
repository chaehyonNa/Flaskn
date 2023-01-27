koreanDict = {'0': '쌀밥', '1': '기타잡곡밥', '2': '콩밥', '3': '보리밥', '4': '돌솥밥', '5': '현미밥', '6': '흑미밥', '7': '감자밥', 'gon': '곤드레밥', 'kimchi': '김치볶음밥', \
    '10': '주먹밥', '11': '볶음밥', '12': '일반비빔밥', '13': '전주비빔밥', '14': '삼선볶음밥', '15': '새우볶음밥', '16': '알밥', '17': '산채비빔밥 ', '18': '오므라이스', '19': '육회비빔밥', \
    '20': '해물볶음밥', '21': '열무비빔밥', '22': '불고기덮밥', '23': '소고기국밥', '24': '송이덮밥', '25': '오징어덮밥', '26': '자장밥', '27': '잡채밥', '28': '잡탕밥', '29': '장어덮밥', \
    '30': '제육덮밥', '31': '짬뽕밥', '32': '순대국밥', '33': '카레라이스', '34': '전주콩나 물국밥', '35': '해물덮밥', '36': '회덮밥', '37': '소머리국밥', '38': '돼지국밥', '39': '하이라이스', \
    '40': '김치김밥', '41': '농어초밥', '42': '문어초밥', '43': '새우초밥', '44': '새우튀김롤', '45': '샐러드김밥', '46': '광어초밥', '47': '소고기김밥', '48': '갈비삼각김밥', '49': '연어롤 ', \
    '50': '연어초밥', '51': '유부초밥', '52': '장어초밥', '53': '참치김밥', '54': '참치마요삼각김밥', '55': '치즈김밥 ', '56': '캘리포니아롤', '57': '한치초밥', '58': '일반김밥', '59': '간자장', \
    '60': '굴짬뽕', '61': '기스면', '62': '김치라면', '63': '김치우동', '64': '김치말이국수', '65': '닭칼국수', '66': '들깨칼국수', '67': '떡라면', '68': '라면', '69': '막국수', \
    '70': '메밀국수', '71': '물냉면', '72': '비빔국수', '73': '비빔냉면', '74': '삼선우동', '75': '삼선자장면', '76': '삼선짬뽕', '77': '수제비', '78': '쌀국수', '79': '열무김치국수', \
    '80': '오일소스스파게티', '81': '일식우동', '82': '볶음우동', '83': '자장면', '84': '잔치국수', '85': '짬뽕', '86': '짬뽕라면', '87': '쫄면', '88': '치즈라면', '89': '콩국수', \
    '90': '크림소스스파게티', '91': '토마토소스스파게티', '92': '해물칼국수', '93': '회냉면', '94': '떡국', '95': '떡만둣국', '96': '짜장라면', '97': '고기만두', '98': '군만두', '99': '김치만두', \
    '100': '물만두', '101': '만둣국', '102': '게살죽', '103': '깨죽', '104': '닭죽', '105': '소고기버섯죽', '106': '어죽', '107': '잣죽', '108': '전복죽', '109': '참치죽', \
    '110': '채소죽', '111': '팥죽', '112': '호박죽', '113': '콘스프', '114': '토마토스프', '115': '굴국', '116': '김치국', '117': '달걀국', '118': '감자국', '119': '미역국', \
    '120': '바지락조개국', '121': '소고기무국', '122': '소고기미역국', '123': '순대국', '124': '어묵국', '125': '오징어국', '126': '토란국', '127': '탕국', '128': '홍합미역국', '129': '황태해장국', \
    '130': '근대된장국', '131': '미소된장국', '132': '배추된장국', '133': '뼈다귀해장국 ', '134': '선지(해장)국', '135': '콩나물국', '136': '시금치된장국', '137': '시래기된장국', '138': '쑥된장국', '139': '아욱된장국', \
    '140': '우거지된장국', '141': '우거지해장국', '142': '우렁된장국', '143': '갈비탕', '144': '감자탕', '145': '곰탕', '146': '매운탕', '147': '꼬리곰탕', '148': '꽃게탕', '149': '낙지탕', \
    '150': '내장탕', '151': '닭곰탕', '152': '닭볶음탕', '153': '지리탕', '154': '도가니탕', '155': '삼계탕', '156': '설렁탕', '157': '알탕', '158': '연포탕', '159': '오리탕', \
    '160': '추어탕', '161': '해물탕', '162': '닭개장', '163': '육개장', '164': '뼈해장국', '165': '미역오이냉국', '166': '고등어찌개', '167': '꽁치찌개', '168': '동태찌개', '169': '부대찌개', \
    '170': '된장찌개', '171': '청국장찌개', '172': '두부전골', '173': '곱창전골', '174': '소고기전골', '175': '국수전골', '176': '돼지고기김치찌개', '177': '버섯찌개', '178': '참치김치찌개', '179': '순두부찌개', \
    '180': '콩비지찌개', '181': '햄김치찌개', '182': '호박찌개', '183': '고추장찌개', '184': '대구찜', '185': '도미찜', '186': '문어숙회', '187': '아귀찜', '188': '조기찜', '189': '참꼬막', \
    '190': '해물찜', '191': '소갈비찜', '192': '돼지갈비찜', '193': '돼지고기수육', '194': '찜닭', '195': '족발', '196': '달걀찜', '197': '닭갈비', '198': '닭꼬치', '199': '돼지갈비', \
    '200': '떡갈비', '201': '불고기', '202': '소곱창구이', '203': '소양념갈비구이', '204': '소불고기', '205': '양념왕갈비', '206': '햄버거스테이크', '207': '훈제오리', '208': '치킨데리야끼', '209': '치킨윙', \
    '210': '더덕구이', '211': '양배추구이', '212': '두부구이', '213': '삼치구이', '214': '가자미전', '215': '굴전', '216': '동태전', '217': '해물파전', '218': '동그랑땡', '219': '햄부침', \
    '220': '육전', '221': '감자전', '222': '고추전', '223': '김치전', '224': '깻잎전', '225': '녹두빈대떡', '226': '미나리전', '227': '배추전', '228': '버섯전', '229': '부추전', \
    '230': '야채전', '231': '파전', '232': '호박부침개', '233': '호 박전', '234': '달걀말이', '235': '두부부침', '236': '두부전', '237': '건새우볶음', '238': '낙지볶음', '239': '멸치볶음', \
    '240': '어묵볶음', '241': '오징어볶음', '242': '오징어채볶음', '243': '주꾸미볶음', '244': '해물볶음', '245': '감자볶음', '246': '김치볶음', '247': '깻잎나물볶음', '248': '느타리버섯볶음', '249': '두부김치', \
    '250': '머위나물볶음', '251': '양송이버섯볶음', '252': '표고버섯볶음', '253': '고추잡채', '254': '호박볶음', '255': '돼지고기볶음', '256': '돼지껍데기볶음', '257': '소세지볶음', '258': '순대볶음', '259': '오리불고기', \
    '260': '오삼불고기', '261': '떡볶이', '262': '라볶이', '263': '마파두부', '264': '가자미조림', '265': '갈치조림', '266': '고등어조림', '267': '꽁치조림', '268': '동태조림', '269': '북어조림', \
    '270': '조기조림', '271': '코다리조림', '272': '달걀장조림', '273': '메추리알장조림', '274': '돼지고기메추리알장조림', '275': '소고기메추리알장조림', '276': '고추조림', '277': '감자조림', '278': '우엉조림', '279': '알감자조림', \
    '280': '(검은)콩조림', '281': '콩조림', '282': '두부고추장조림', '283': '땅콩조림', '284': '미꾸라지튀김', '285': '새우튀김', '286': '생선가스', '287': '쥐포튀김', '288': '오징어튀김', '289': '닭강정', \
    '290': '닭튀김', '291': '돈가스', '292': '모래집튀김', '293': '양념치킨', '294': '치즈돈가스', '295': '치킨가스', '296': '탕수육', '297': '깐풍기', '298': '감자튀김', '299': '고구마맛탕', \
    '300': '고구마튀김', '301': '고추튀김', '302': '김말이튀김', '303': '채소튀김', '304': '노각무침', '305': '단무지무침', '306': '달래나물무침', '307': '더덕무침', '308': '도라지생채', '309': '도토리묵', \
    '310': '마늘쫑무침', '311': '무생채', '312': '무말랭이', '313': '오이생채', '314': '파무침', '315': '상추겉절이', '316': '쑥갓나물무침', '317': '청포묵무침', '318': '해파리냉채', '319': '가지나물', \
    '320': '고사리나물', '321': '도라지나물', '322': '무나물', '323': '미나리나물', '324': '숙 주나물', '325': '시금치나물', '326': '취나물', '327': '콩나물', '328': '고구마줄기나물', '329': '우거지나물무침', \
    '330': '골뱅이무침', '331': '김무침', '332': '미역초무침', '333': '북어채무침', '334': '회무침', '335': '쥐치채', '336': '파래무침', '337': '홍어무침', '338': '골뱅이국수무침', '339': '오징어무침', \
    '340': '잡채', '341': '탕평채', '342': '갓김치', '343': '고들빼기', '344': '깍두기', '345': '깻잎김치', '346': '나박김치', '347': '동치미', '348': ' 배추겉절이', '349': '배추김치', \
    '350': '백김치', '351': '부추김치', '352': '열무김치', '353': '열무얼갈이김치', '354': '오이소박이', '355': '총각김치', '356': '파김치', '357': '간장게장', '358': '마늘쫑장아찌', '359': '고추장아찌', \
    '360': '깻잎장아찌', '361': '마늘장아찌', '362': '무장아찌', '363': '양념게 장', '364': '양파장아찌', '365': '오이지', '366': '무피클', '367': '오이피클', '368': '단무지', '369': '오징어젓갈', \
    '370': '명란젓', '371': '생연어', '372': '생선물회', '373': '광어회 ', '374': '훈제연어', '375': '육회', '376': '육사시미', '377': '가래떡', '378': '경단', '379': '꿀떡', \
    '380': '시루떡', '381': '메밀전병', '382': '찰떡', '383': '무지개떡', '384': '백설기', '385': '송편', '386': '수수부꾸미', '387': '수수팥떡', '388': '쑥떡', '389': '약식', \
    '390': '인절미', '391': '절편', '392': '증편', '393': '찹쌀떡', '394': '매작과', '395': '다식', '396': '약과', '397': '유과', '398': '산자', '399': '깨강정'}

def change(label):
    if label in koreanDict:
        return koreanDict[label]