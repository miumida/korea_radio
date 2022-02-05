DOMAIN = "korea_radio"

#EBS FM
EBS_URL = "https://ebsonair.ebs.co.kr/fmradiofamilypc/familypc1m/playlist.m3u8"
EBS_ARTWORK = 'https://github.com/miumida/korea_radio/blob/main/cover_image/EBS_FM.png?raw=true'

#MBC
MBC_BSE_URL  = 'http://miniplay.imbc.com/WebHLS.ashx?channel={}&protocol=M3U8&agent=ios&nocash=0.3996827673840577&callback=jarvis.miniInfo.loadOnAirComplete'
MBC_CALL_URL = 'http://175.158.10.83/s{}/_definst_/{}.stream/playlist.m3u8?{}'

FM4U_ARTWORK    = "https://github.com/miumida/korea_radio/blob/main/cover_image/mbc_fm4u.png?raw=true"
MBCFM_ARTWORK   = "https://github.com/miumida/korea_radio/blob/main/cover_image/mbc_mbcfm.png?raw=true"
ALLTHAT_ARTWORK = "https://github.com/miumida/korea_radio/blob/main/cover_image/mbc_allthat.png?raw=true"

_MBC_CH = {
    'mbcfm4u' : 'mfm',
    'mbcfm'   : 'sfm',
    'allthat' : 'chm'
}

_MBC_CH_PARAM  = {
    'mbcfm4u' : [ 'MBC FM4U',     FM4U_ARTWORK    ],
    'mbcfm'   : [ 'MBC 표준 FM',  MBCFM_ARTWORK   ],
    'allthat' : [ 'MBC all that', ALLTHAT_ARTWORK ]
}

FM4U_SCH = {
    '00' : [ '배순탁의 B side',                  '' ],
    '01' : [ '신혜림의 JUST',                    '' ],
    '02' : [ 'FM영화음악 김세윤입니다',          '' ],
    '03' : [ 'K팝2000',                          '' ],
    '04' : [ 'K팝2000',                          '' ],
    '05' : [ '세상을 여는 아침 김정현입니다',    '' ],
    '06' : [ '세상을 여는 아침 김정현입니다',    '' ],
    '07' : [ '굿모닝FM 장성규입니다',            '' ],
    '08' : [ '굿모닝FM 장성규입니다',            '' ],
    '09' : [ '오늘 아침 정지영입니다',           '' ],
    '10' : [ '오늘 아침 정지영입니다',           '' ],
    '11' : [ '김현철의 골든디스크',              '' ],
    '12' : [ '정오의 희망곡 김신영입니다',       '' ],
    '13' : [ '정오의 희망곡 김신영입니다',       '' ],
    '14' : [ '두시의 데이트 뮤지, 안영미입니다', '' ],
    '15' : [ '두시의 데이트 뮤지, 안영미입니다', '' ],
    '16' : [ '오후의 발견 이지혜입니다',         '' ],
    '17' : [ '오후의 발견 이지혜입니다',         '' ],
    '18' : [ '배철수의 음악캠프',                '' ],
    '19' : [ '배철수의 음악캠프',                '' ],
    '20' : [ '전효성의 꿈꾸는 라디오',           '' ],
    '21' : [ '전효성의 꿈꾸는 라디오',           '' ],
    '22' : [ '푸른밤, 옥상달빛 입니다',          '' ],
    '23' : [ '푸른밤, 옥상달빛 입니다',          '' ]
}

#CBS
CBS_SFM_URL    = "http://aac.cbs.co.kr/cbs981/_definst_/cbs981.stream/playlist.m3u8"
CBS_MFM_URL = "http://aac.cbs.co.kr/cbs939/_definst_/cbs939.stream/playlist.m3u8"

#SBS
SBS_BSE_URL = "https://apis.sbs.co.kr/play-api/1.0/livestream/{}/{}?protocol=hls&ssl=Y"

SBS_ARTWORK_POWERFM = "https://github.com/miumida/korea_radio/blob/main/cover_image/sbs_powerfm.png?raw=true"
SBS_ARTWORK_LOVEFM  = "https://github.com/miumida/korea_radio/blob/main/cover_image/sbs_lovefm.png?raw=true"
SBS_ARTWORK_SBSDMB  = "https://github.com/miumida/korea_radio/blob/main/cover_image/sbs_sbsdmb.png?raw=true"

_SBS_CH = {
    'powerfm' : 'powerpc',
    'lovefm'  : 'lovepc',
    'sbsdmb'  : 'sbsdmbpc'
}

_SBS_CH_PARAM  = {
    'powerfm' : [ 'SBS POWER FM',   SBS_ARTWORK_POWERFM ],
    'lovefm'  : [ 'SBS LOVE FM',    SBS_ARTWORK_LOVEFM  ],
    'sbsdmb'  : [ 'SBS 로릴라디오M',   SBS_ARTWORK_SBSDMB  ]
}
