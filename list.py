
import streamlit as st
st.set_page_config(
    page_title = '持ち物リスト')
st.title("幼稚園持ち物リスト")

type_ = st.selectbox("保育時間は？",["午前","1日"],index=None,
   placeholder="保育時間を選んでください...")


if type_=="1日":
  day = st.selectbox("何曜日？",["月","火","水","木","金"],index=None,
   placeholder="曜日を選んでください...")
  cal = st.selectbox("カリキュラムは？",["音楽","体育","英語","お茶","なし"],index=None,
   placeholder="カリキュラムを選んでください...")
  club = st.selectbox("課外活動は？",["音楽","英語","書道","体操","絵画","なし"],index=None,
   placeholder="課外活動を選んでください...")
  month = st.selectbox("何月？",["4月","5月","6月","7月","8月","9月","10月","11月","12月","1月","2月","3月"],index=None,
   placeholder="月を選んでください...")
f"　↓↓↓準備する持ち物↓↓↓"
if type_=="午前":
    st.write("体操服・ランチョンマット・エプロン・コップ・水筒・出席ノート")

if type_=="1日":
  st.write("体操服・ランチョンマット・エプロン・コップ・お箸・水筒・出席ノート")
  if day =="火" or day =="木":
    st.write("お弁当")
  if day =="月":
    st.write("上靴・運動靴・スモック・カラー帽子")
  if cal =="音楽" or club=="音楽":
   st.write("ピアニカ")
  if club =="書道":
   st.write("書道セット")
  if club =="絵画":
   st.write("絵具セット")
  if month =="6月"or month =="7月"or month =="8月"or month =="9月":
   st.write("ループ付きタオル")
  if cal =="体育":
   st.write("★体操服登園★")
  if cal =="体育"and club !="体操":
   st.write("制服(体操服袋に入れる)")













