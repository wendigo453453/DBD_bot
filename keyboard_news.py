from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import json

with open('news/news_dict.json', 'r') as file:
    data = json.load(file)

with open('news/leaks_dict.json', 'r') as file:
    datal = json.load(file)

news_main = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('📬DBD NEWS📬')
b2 = KeyboardButton('📬💧DBD LEAKS💧📬')
b3 = KeyboardButton('⬅️back to main menu')
news_main.add(b1, b2, b3)

ikb_dbd_news1 = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n1")
b2 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n1->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['0']['news_link']))
ikb_dbd_news1.add(b1, b2, b4)

ikb_dbd_news2 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n2")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n2")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n2->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['1']['news_link']))
ikb_dbd_news2.add(b1, b2, b3, b4)

ikb_dbd_news3 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n3")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n3")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n3->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['2']['news_link']))
ikb_dbd_news3.add(b1, b2, b3, b4)

ikb_dbd_news4 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n4")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n4")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n4->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['3']['news_link']))
ikb_dbd_news4.add(b1, b2, b3, b4)

ikb_dbd_news5 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n5")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n5")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n5->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['4']['news_link']))
ikb_dbd_news5.add(b1, b2, b3, b4)

ikb_dbd_news6 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n6")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n6")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n6->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['5']['news_link']))
ikb_dbd_news6.add(b1, b2, b3, b4)

ikb_dbd_news7 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n7")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n7")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n7->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['6']['news_link']))
ikb_dbd_news7.add(b1, b2, b3, b4)

ikb_dbd_news8 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n8")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n8")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n8->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['7']['news_link']))
ikb_dbd_news8.add(b1, b2, b3, b4)

ikb_dbd_news9 = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n9")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n9")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n9->")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['8']['news_link']))
ikb_dbd_news9.add(b1, b2, b3, b4)

ikb_dbd_news10 = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n10")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n10")
b4 = InlineKeyboardButton(text='read in source',
                            url=(data['9']['news_link']))
ikb_dbd_news10.add(b1, b2, b4)







ikb_dbd_news1_l = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n1_l")
b2 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n1->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['10']['news_link']))
ikb_dbd_news1_l.add(b1, b2, b4)

ikb_dbd_news2_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n2_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n2_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n2->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['11']['news_link']))
ikb_dbd_news2_l.add(b1, b2, b3, b4)

ikb_dbd_news3_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n3_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n3_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n3->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['12']['news_link']))
ikb_dbd_news3_l.add(b1, b2, b3, b4)

ikb_dbd_news4_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n4_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n4_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n4->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['13']['news_link']))
ikb_dbd_news4_l.add(b1, b2, b3, b4)

ikb_dbd_news5_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n5_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n5_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n5->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['14']['news_link']))
ikb_dbd_news5_l.add(b1, b2, b3, b4)

ikb_dbd_news6_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n6_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n6_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n6->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['15']['news_link']))
ikb_dbd_news6_l.add(b1, b2, b3, b4)

ikb_dbd_news7_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n7_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n7_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n7->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['16']['news_link']))
ikb_dbd_news7_l.add(b1, b2, b3, b4)

ikb_dbd_news8_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n8_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n8v")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n8->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['17']['news_link']))
ikb_dbd_news8_l.add(b1, b2, b3, b4)

ikb_dbd_news9_l = InlineKeyboardMarkup(row_width=3)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n9_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n9_l")
b3 = InlineKeyboardButton(text='next news➡️',
                                  callback_data="next_n9->_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['18']['news_link']))
ikb_dbd_news9_l.add(b1, b2, b3, b4)

ikb_dbd_news10_l = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='⬅️previous news',
                                  callback_data="<-previous_n10_l")
b2 = InlineKeyboardButton(text='read more',
                                  callback_data="read more_n10_l")
b4 = InlineKeyboardButton(text='read in source',
                            url=(datal['19']['news_link']))
ikb_dbd_news10_l.add(b1, b2, b4)