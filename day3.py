import re

raw_string = """
what()-%*;[mul(826,659)what()&mul(622,241)}^from();why()mul(499,923))mul(589,186)~how()why()]/~who()}mul(57,224)* ##[[*>mul(206,45)select(){~from(63,961)+!/'@mul(365,743)^ from()mul(94,410)$how()(^ )/,mul(592,884) mul(265,485))^#[[mul(763,659),mul(275,537)$;who()*mul(511,392)))what()(+from()from()>&-mul(416,947)mul(868,183)?:where()*when()#-where(890,406)#-mul(873,379)mul(195,835)/,%?],!-{(mul(225,902)where()'(where()-@#mul(544,955)how();~when(222,774)mul(538,277),from()from(717,816)$)(!%select()mul(247,162)**why()!}/where()mul(411,570)]mul(158,805)<[)}!@$select()don't()&?mul(475,153)when()mul(44,394)mul(505,328)select(),;[+mul(228,58)}/)why()?who()mul(706,785)$!#mul(635,796)#[where(){^select(275,150)-/)mul(85,214)<when()/*&where()mul(438,107)who(); what()why()why()mul(556,985):-+;@why()}?mul(581,266)why() %mul(570,646)what();@<$mul(626,256)#>do()where()@'<mul(42,958)#{mul(980,871) ,:{^!>mul(651,67)]-mul(530,38)why()+^don't(),where();what()~mul(532,711)<how()-;(^mul(538,343);mul(403,312)#where()select()<}mul(160,441) (mul(35,591)from()mul(458,977)mul(682,17)who()select()!^ :how()from()!~mul(698,638)'<@;'where()'from()!select(458,218)mul(80,356)^,what(554,850)*<&what()select()select()do()>,;)$why()+what();%mul(265,354)-mul(338,874)?]mul(284,884)}<when()mul(473,399)%>'?where(),mul(614,138)&who()~}[why()from()mul(779,747)^mul(7,27)select()}>+^-*<mul(808,414) &)when()[;&mul(969,162):where(){mul(923,581))*when()who()}?mul(604,624)**mul(968,780)):/{mul(808,433)]!who()from()mul(103,80)@^why()!mul(335,504)&how():how()}mul(407,608)'+mul(350,417)select()>who()*mul(545,113)who()('!&how(),don't()+{$&mul(842,42)<#mul(788,22),why(),mul(581,843)why()?mul(415,102)[mul(782,483)::(&',^mul(411,597)mul(800,946)[]($}:+)]mul(6,738)who()+where()@}(where()>$when()mul(737,227)select()~ why(984,422)mul(690,299)$how()!why()when() why()>:who()mul(62,391)mul(559,901)mul(152,669)([why()-select();*(mul(674,497)mul(195,917)from()#what(),mul(332,868)select()')@#mul(957,359)(when()]>(<what()!mul(602,990)+@how()]$^mul(885,543)mul(564,365)mul(912,603)what()when()how()mul(216,398+&#'*-,]:mul(971,792)!do()from()who()mul(741,501)~how()where()<what()[#where()mul(268,825)what()mul(958,990)){?(+'mul(427,368):%?how()?(mul(725,420)?when()}-from();mul(414,122/%-when():-'@mul(450,900)&what()<{ ]<'(?do()%]^!} mul(401,278)when() -(! -do()when()*select()?@[~@from()why()mul(892,125)~what()+;/mulwhy():mul(375,500)^(#>%,mul(252,836)[why()?<how(643,18);*mul(223,308)$where()mul(401,278)why():mul(276,426)mul(793,320)what(85,700)})mul(485,616)where();when()}[! from();]mul(582,705) !:mul(427,563)<*<#how():!do()'&-}!']:'mul(615,412)where(928,116)];select()(mul(812,857)&@?[select()$~do()mul(49,314)?{mul(164,850)mul(345,646)[}from()}]<'#select()don't()<;+%where(445,34)*!mul!when()-{mul(471,900)<[-from()&@mul(442,893)where())*mul(798,495)}<+select(130,600)why()(from()mul(860,565)select()~why(406,274)mul(397,514)who()why()]~mul(654,583>where()!,mul(877,551)&select()[<?&{}when(){mul(528,802),#-)+(&select()/mul(878,466)#how(872,781)mul(964,641>}->(*[mul(847,681),why()select()select()*@,mul(211,86)when()select()-:)#']mul(416,630):(}?$[:)mul(255,942):-*:!~%@how()what()mul(117,324)
/}mul(804,424)mul?where())%}mul(933,657)%from()what()'~!}*:mul(916,775)who()<select()<how()don't()#from(773,402);/,when()mul(425,484)> {,what(485,199)when()#mul(760/-select();mul(859,259) )?mul(21,933)what()^from()#-mul(951,427)don't()<!mul(664,380)mul(747,497)*who()}from()*+mul(505^) <#:select()]?select()mul(383,587)*mul(747,795)how()where()who()&}#:mul[@%mul(488,640)how()who()^'>mulwhere(295,787)%'~*who()@mul(500,697)where()*^!@^what():mul(737,496)^{)^how()when()#mul(387,233)']%select();}mul(89,882)}(&mul(394,392)#from()what()}who()when()when()>;^mul(639,188) [*mul(302,818)[mul(874,794)~{(<>[%mul(217,113)~why() mul(651,680)^!/'select()mul(161,158)'}/*{mul(41,452)?;;@,[~}why()mul(71,555)<select()%:when()]@what(198,130)do()mul(364,266)*+)what(65,6)'mul(503where()'{what()?mul(84,10)/;''^;mul(180,571)how()(]mul(804,566)>who()}]where()*%where()?mul(909,630)%^where()how()'mul(678,912)*)+what():don't()*^[$mul(208,358)mul(99,216,??/-%]when(40,18)>'(mul(967,259)^!%!mul(574,337)mul(855,993)from()who()<@ -&mul(679,566)[;$how()mul(773,340)+-':-mul(46,577);>+%^#mul(668,549)@;#,[])don't()mul(471,350)why()?what()where()what()</[mul(725,898):(-mul(869,478)%don't()'mul(896,319)]from(){@don't(),,why(){what(394,834)?mul(58,736)%#/ <mul(51,867)*)^why()#'mul(176,298)$where()//>,]:!where()mul(474,215):#what():%}how():mul(47,116)-,^from()?[select()>mul(566,323);!$why()what()<>{%-mul(756,641)(]{what()$>@#$%mul(478,68)!](;@+when()mul(383,83)>>@ do())(/!when(){{)~when()mul(18,568)mul(933,58))mul(53,523)what()where()>+where()^mul(847,728)>where() who()how()]mul(499,856)mul(837,413)&:who();from()@mul(711,785)@from()select()$]#-}mul(603,647)!how()'}/mul(142,83)mul(236,987)(&[)+$<&when()mul(464,484)[mul(97,923{[{;~*how(603,347)why(397,750)[mul(397,378):from()who()@$[mul(33,741)@&<['from():do()]select()/!who()from()what()(+mul(425,204)<[^select()#:?do()/mul(977,606)how()select()?select() ^mul(481,671)^&,)&what()select()from()from()mul(219,42):what()?}mul(441where()({select(),mul(333,910)from()from()where()]*'mul(925,221):%?from()mul(981,324)%}mul(595,648)&select()/mul(742,838)when()~@from()don't()#+)(<^?}mul(554,328)} -?(mul(513,192)~~$*why()/~% mul(444,631)## mul(794,537)-#what()~how()why(310,427)(mul(781,606)< from()<mul(674,614)where()when()how(){who()when()where()where()what()mul(416,867)$!!why(54,460)^when()mul(153,262)]where()what()who()]'do()mul(179&$)%>@&mul(787,800)@how(266,66)<?~&,{mulselect()<>-{when()what()who()mul(538,246)[^*+why()where()mul(629,836)from()* [$+&]mul(77,354)%]:from()mul(260,304)@why()!/when()where()+(mul(354,804) mul(76,15)>mul@!!$]from()mul(357,50)(mul+%~]$-%%don't()(from();when()#;~when()mul(564,123)~&]<mul(985who()#mul(269,732)(mul(963:^mul(824,4)$*how()@%what() -%mul(891,926)^*how()?select()->@mul(489,580from()what(95,431)+:*- ,*'mul(745,620)how()'why()>-from()[?><mul(509,286)->!!mul(988,840))^)(]<mul(657,220)who()[;when()>]#^}mul(298,967)when():who()#who()what()mul(84,148)< ;&@^do()when()~^where()#^$mul(341,853)<+~*what(252,434)*{{mul(986,313)]&>&>mul(620,476)why()who()mul(69,875<$-&(''mul(106,787)mul(171,707)who();~when()+>;how();+mul(163,282)(];?>}* mul(571,602)/from()+/]!{+mul(372,949)$?*$(mul(921,212)@'>mul(705,437)($when()where()mul(371,384)>mul(445,760)'do()?/when()%[^mul(382,44)}&/)&$select()mul(284,899) when():%mul(554,813)$;~>mul(274,983)'')?-from()mul(668,571)when()why()mul(981,529)>where()%) #& [^mul(864,321)how()'[mul(752,285)$ mul(448,366)&why()])${;^from()who()mul(251,944)select()-&*mul(724>>)}^,select()~~}do()}))%who()#mul(652,853)
mul(914,760)%]how())mul(325,361)>[@#{mul(49,627)> []!%?@:mul(866,756)!?^how()#select()(}&mul(217,708)>mul(534,113)<()(~(how()&mul(522,207)where() who()why())]mul(549,286)what(824,300)-]when()]}:select()mul(536,959$(~#&*[~})mul(47,72){:mul(907,280)&!mul(175,322)mul(460,379)select()'?&mul(697,154){^%[^from()when(552,273)mul(454,997)*&/mul(514,858)$why(29,970): ,+!<&mul(411,897)[%why(),mul(749from()where())+ <mul(565,182)>]how()'what()mul(739,713)mul(116,113)mul(203,704)/!select(379,766)]&when()^from()#mul(903,203)!,!< {%]?mul(330,707)where()(+how()>mul(526,973)~]^&'how()mulfrom() +];mul(964,967)@why()from()when()^~ mul(217,465)]from()/from()@&]where(263,584)+why()mul(267,301)}when():#don't()>who(860,416)<select()&mul(552,955)]@mul(830,261!% /-(why()when() ^mul(577,681) where(145,770)why()where()mul(604,697)]$[,mul(784,378);(@where(413,20)why()don't()#)/#mul(32,109;mul(212,539)<]>/,mul(126,52);<}+[who(),where()mul(868,540)when(332,336)mul(134,939)#mul(119,818)mul(777,396)+mul[mul(184,9)select()mul(375,842)]mul(527,499)~#what()'mul(260,652)mul(15,171)what()mul(273,578)-?mul(798,178)&?<;#%:mul(886,756)where()who()~^,from()$mul(775,238)[why()'mul(229,247)/mul(105,511)from()?]>+/why()$!:mul(578,64)?where()*)~:&( where()mul(917,699)&:~^'~who()mul(685,592); ,where()%[{mul(535,245)' why()*mul(166,874)!'who()why()/~:}-what()mul(430,972)[(mul(11,883)>?-%<when(560,496)$*mul(398,75):/why()^]where()mul>/#;who(382,885)why()}where()*&?mul(142,204),!why()from(805,222),mul(165,77>>from()mul(539,602)@- !!from()where()>mul(725,894)#mul(664,363)mul(436,916)(;*]!/mul(276,69)?^~how()?:-what()do()mul(174,136)where() ,#:*)mul(465,302)*!-why()^/mul(363,643)})(why()!mul(149,621))^*?who(),mul(172,73)mul(631,398)]from()mul(998,161)@[[@who()?mul(310,639)#-}{what()?;!(mul(584,757)~ !(do()$->#[)$(mul(124,565){mul(698,142)}})-mul(742,227)%#why()/,$:select()mul(152,975)why()*&?~#'~*?mul(908,265)mul(620,516)from()select(209,291)why()$mul(539,160);select()~}*{when()mul(784,853)who(15,285);where(),^;where()-[mul(342,770select()*;>-((*&mul(982,965)how()&mul(523,830)when(961,246)[ why()+why()]mul(785,203)who(99,69),*mul(936,742)?^','%;-why()!mul~)when()when()select()!(;&@how(900,734)mul(589,321)mul(964,282)-))how()why()what()(*})mul(47,984)@mul(253,826)mul(429,558)where()how();<#what()#+mul(983,307)~>}-)/who()mul(327,880)+}when(){when()}mul(593,869)mul(643,89)-:,,,<;mul(33^who()[)+-^mul(189,550)<:mul(519,574)*how()?where()[^;when()mul(563,151select()-what()]mul(574,867))}mul(800,881)who()'#~#mul(46$mul(693,762)-!@,#mul(454,19)$!select()from()*who()),mul(269,371)from()mul(330,479)%&!}how(477,247) [do())why()^}+''-how()mul(819,485)how()-)~*%what(447,325)why()mul(462,456)#?]mul(912,654)]mul(2,822)$)>':select()when()select()/]mul(557,454)'%<>+%what())*do()when()why(716,84)@/mul(89,140)select()('mul(310,84),*select(),$?mul(86,400)[/what()<@~$mul-!when()who()%#where()'[who()(mul(755,653)mul(594,757from()from()<[,;mul(916,545)mul(206,9)@$)mul(588,12) '][)select()$from()from(220,871)@mul(849,103)-/mul(887,921)$#who()who()mul(873,831):why()}who()[+mul+&>#how()how() : mul(323,651)why()!mul(620,114)<+what(844,679)/{/*mul(327,69)mul(472,982)how()^(mul(321,807)when()why()]why()$mul(694,629)/%/ who()*[mul(648,109)]>[''@mul(543,595)${{{:>;#!/usr/bin/perl ]-(#:how()]<+mul(770,832)
$select()when()@*)&select()how()/mul(195,671)';;^(select()!mul(342,663)@$@%~)>)don't()what()mul(681,868)-@who(237,633)}when())*#>;mul(532'select(828,390);what(),<%?-:{mul(835,208)%/$select(21,874)mul(214,27)from()who()who()/mul(767,769)!~,+>who()<who()how()from()mul(378,284)mul(303,165)select(),%mul(550,216)(>,mul(204(}who()!when(940,779)<$from()^mul(944,886)mul(714,285)<)~~why()mul(352,872)what():/mul(419,248)#from()&select()>>mul(557,809)-why()from():mul^?);mul(231,230)(what()%/:{mul(635,952)mul(896,753)-&*%mul(475,955))[when()(&~}mul(865,939)mul(557,651) !)~:mul(172,689)/from()]{$,;what()mul(956,624):[,@+}what()mul(601,236))where()*from()from()mul(820,982)who()$select()when()/<when()mul(949,607):~-$mul(321,684),&&~mul(847,261)mul(726,906)[!@where()<*how()*#;mul(192,221)'from()select()what()%mul(832,291)mul(975,738) ,~mul(152,341)don't()*%mul(792,874)]where()@;mul(390,16)mul(285,187),mul(26,776)why():$#},select()mul(346,341))how():where()^/mul(899,379) }^,who()~select()!mul(105,998)how(18,23)<(select()mul(565)@]select():(when()mul(988,676);?mul(825,122);how()from():{)>mul(249,654)#,from():;!don't()}+select();/why(240,203)where()^!mul(373,721)from()?,mul(234,262)how()'>([mul(477,58)mul(161,422)~mul(985}/select()-~mul(344,788);mul(660,334)do()when()]where()&who()when(){mul(955,809)+who()>how()where()?-^/mul(800,971) mul(331,999)[{where(){}]@!mul(243,886)<mul(530,831)what()when() how(995,815)where()+,)!&mul(545,505)&:%(;mul(291,529who()where()[-{{-what()'>mul(807,365)why(708,402)@when()?who()mul(242,464)&^,[{how(){when()*(mul(593,164)&*/&where()select(237,204)mul(474#/<mul(376,919)when()how()where()/?'){mul(547,382);who()# )>mul(533,804)&, how()why(653,768)mul(489,173)]where()from()[&{?:mul(62,23)& )where()from() mul(234,284)@who()why()* }*mul(938,464)from(),+?(@why()   don't()what(338,233)?~'+who()$@mul(63,606):mul(713,654)$from()(+&:mul(138,999);&#select()<select()-*who()[mul(925,57)when()&[<why()*where(221,603)~/mul(841,865)'why()%<mul(86,164)mul(226,558)!(:+(how()who()mul(193,897)where()#!}mul(939,962)%,why()(!'>~mul(432,589)?>^(?*&mul(117,404)@)where()why(6,662)mul(942,298)mul(16,588)how()<mul(261,707)<why()when()why(){~&%@mul(593,32)^mul(388,286)who()*%-mul(25,840)why() *}mul(972,967)]~mul(669,616),-;{mul(29,722)-/$<why(164,698)mul(440,168)who()-what()how()@^@}:mul(396,626)>*~<~ from()-mul(610,545):why()#]-;how())what()}mul(977,824)??when()mul(241,702)!^]@mul(98,19)!{what()mul(896,817)?who())^#&;:?mul(475,309){]~<what()select()-when()mul(249,917[when()[(([/where()select()mul(26,324):^!how()mul(978,685):%(+}/mul(138,943),how()+<?who()@>!who()mul(819,280)+~why(22,676)mul(714,597)from()when())^~+, mul(962,748)%mul(178,691)<from()@@>$what()mul(777,740)&who())where(),;mul(632select()/ *who()who()@mul(460,751)+',mul(862,580)# :-what()!+{don't():$!<^:from(){&who()mul(93,231)how()select()#+)-^don't()/&>*#'/&[<mul(287,405)!/'mul(590,513)from()mul(801,217)*from(10,240))>(;&>,from()do(),what())what()$*mul(742,889)mul(62,478)?[why()why(),mul(837,195)why(){>,$@!'mul(722,317)%%select()when()what()(('/+mul(251),)<mul(591,577)who():#*&#[@mul(605,108){ how():select()$#select()where();mul(386,407)+}[mul(283,172))<select()from()#+{{!mul(379,555,)*>>mul(148,406);don't()when()'mul(784,101)<[!^(where(365,573)<${mul(535,827):{*#mul(335,673)]]^:^]when(222,2)[mul(704,190)!from()who(){%(&} mul(407,649)+~:why()mul(575,579)@}:why()mul(945,425)[what():mul(42,200)
/select()who()how()select()~when(364,150)mul(790,347)+,):+?mul(498,67)!!<'when()}',{mul(440,393)from(283,600):@[ :&mul(584,602)[*%+mul(913,926)(+from()why()(><,$ mul(4,866)where(){;+,why(),when()why()when(199,14)mul(370,854)why()^mul(665,756),>}*{:&when()-how(582,503)don't(){@^,@/mul(306,251)mul(2,820)~&[[^ mul(135,961){~!)mul(526,875)how()+what()?]mul(379,321)%why()%,who()^?don't(),select()%when()mul(476,779)select()mul(811,466)}~~%mul(389,923)>what(){&> :{>mul(806,620)mul(976,304)when(); :)/[mul(463,959)'when()[select()(^]mul(911,997)-%[*,mul(448,155)({from(10,578)mulwhat()when()<}select()(mul(492,179)+from(771,314)<mul(821,553)select(),why()how()why()how()who()select();[mul(755,27)}who()mul(595,676)}^;why()?)!mul(716,763)]{*~when()@;mul(389,65)where()where():how()select()mul(977,258)~(<<what()}(what()mul(165,261)how()when()/,mul(237,121)%mul(442,192)from()%mul(149,123)from()select()how()-why()mul(280,322}why(996,110)<mul(949,404)-mul(190,792)mul(85,466);why()>)&*:!]mul(624,243)who()how()(^&{%+$do()'?mul(171,189)who()where()mul(531,756)@what()who()}mul(83,163)> @)*mul(575,765)why()'$$<mul(794,127,mul(628,236)~,:mul(375,718)$@]mul(184,164)]$?mul(374,308#*mul(652,890)?-*,mul(394,73)~select()mul(37,351)#don't()!%#:when()mul(417,948)? &mul(571,57)?'when()select()@!when()mul(52,129)['/,#mul(609,910)!mul(734,504)?;mul(41,15)('what();why()select()mul(939,660)/%%/)*-don't()mul(393who()?!>who();{who():?+mul(644,730)~from()&/where()select(574,686)what()^?~mul(998,26)~<: [){}?do()how(851,386)#mul(29,770)]what()select(),^why()from(577,917)?/do() mul(309,161),#mul(684,763){#;why()$+[@]mul(99,693)who();(>select() don't()~^,mul(144,109)!@mul(757,540)  <mul(635,426)mul(287,390)-[}?from()-&mul(641,514)/what()&@who():#>+mul(649,668),[^/~> &what()mul(948,181)(what()select()~mul(147,215)mul(790,557)+@when()who()>-{%mul(809,499)+from() mul(594,964)?select()) } ,%mul(105,293)mul(800,358)who())/{$select(343,382)>+from()>mul(556,232)mul(719,487)'&^?why()?^+mul(986]:why()<mul(31,917))mul(181,375)(mul(443,827)why()when()~select(148,144)mul(349,642){]>&mul(487,944)#/>[when()when())<mul(105,877)?#mul(442,949)^}?'&^+when()who()mul(764,156)mul(429,548)]@select(926,250)%;$/^>mul:select()what()&]>^~mul(356,737)$why()^~why()[>mul(357,835)from()~~$+&don't()mul(243,897)mul(606,944);--how() mul(200,517):?:?#),>who()}mul(588,55)&where() how()-:'when()^>mul(144,286)<%{} select()mul(957,918)!mul(901,352)!],;who()>mul(840,776)(,how(544,497)!#:/mul(319,341):what(836,872)<;!!,(!mul(182,549)~mul(550,899)what()>{}^%[do()when()- mul?-('[~@who()~&~mul(376,145)]#]mul(206,452)%?'{+ &how()#]mul(210,898)^+[from()why()'@]/mul(914,474)mul(814,374)how()?mul(679,233select()!$;)*why()who(),{mul(109,898)^^,$^who()what()mul(526,786)what()mul(966,480)mul(971,34)!who()mul(268,920)when(),!^+:!~~don't()'mul(324,732)why(98,537)where()^];}&*mul(341,746)/-+who()(mul(557,763)how()mul(30,249)mul(646,653)'where()(? ,,what() !mul*}&+when()when(579,74)what()]mul(100,419)%*,~-;*~mul(980[who()$where()({do()$)]*mul(154,681):)~select()>'select(110,162)/mul(499,447);~ ]!/%from()mul(140,215)'how()]>^&'/mul(54,832)<mul(654,364)&how()?-- #mul(445,723+select()?'mul(146,179)mul(127,447)(mul(970,298)where()>:*/from()/mul(176,59)@$$[#^]mul(802,12)~mul(85,515)
@)::-from()who()mul(979,36)mul(966,513@+'}?don't()mul(428,358)+where()select(943,219)-?>mul(258,3)what()mul(415,26)/'mul(7,129)@who()how(){mul(104,970)]mul(626,872)where())&mul(349,194) *when()how()%&}(why() mul(827,914) how()[+what()^--[!mul(421,153)?mul(161,508):+where()mul(786;#(@/mul(857,712)why(841,104)[})&from()mul(411 ]how(223,310)mul(528,703) ]mul(17,407):*~+)mul(129,256]%$where()~mul(934,438)~where()&+#what(15,14)$select()mul(170,110)mul(367,246)@ mul(759,593));$' where()why(326,790)?why(101,864)~mul(941,890)what(863,919)}<mul(499,900)>>mul(291,785)where()~when()/what()when()mul(599,49)why()'what()}}/what()%{do()$?why()&what()'mul(235,289)<mul(567,598)what(940,872)#!'#mul(558,233)what()-'-how(18,51)@%how()mul$$what()~~mul(753,714)why():,mul(308,180)where(153,49)when()why()}>mul(326,542)-[why()>[;mul(539,793)mul(608,380)from()>- &:where()<?who()mul(111,200)(?^why()<:%how()&>mul}who()'*;:'how()from()mul(732,637)&>mul(66,802)*mul(549,82)>&from()+!who(809,63)mul(247,247):why();-select()}mul(70,653)] where()>$mul(436++mul(489,212)><}what()[what()when(279,911)mul(135,755)where():;#%$mul(961,126)#:why(),&select()where()mul(952,400)#~{~]/];from()mul(323,62)<#(]mul(216,941))mul(463,878):!+, -;how()mul(955,874) %: $',don't()<#,@$@-#>mulwhere()when()mul(414,753)/%$mul(121,719)?mul(461,998);,(;(@]mul(197,230)(#@who()]who()mul(843,541)%~}mul(444,889)what()~mul(351,825)#?how() *)}@!mul(903,612)from()-+>do()}#*+'{why()^who(469,233)mul(350,416) }where()#,mul(555,729)who()]&mul(688,456)select(818,922);*don't()]who(441,198)?mul(712,946)!)+-  mul(224,129)who(){'!,what()mul(716,626)select()#(mul(26,417) )<what()~%)mul(507,65))mul(185,144)@^&*&:*!)mul(156,922)[who()@;mul(448,420)who()[,how()mul(705,34)why(923,293)#mul(779,33)[?}why()how()$ !mul(565,19)what()>when()+{@@^don't()+*/mul(141,786)(from()[select()]$#>%mul(889,476):why()><from()what()how()why()^mul(100,7)& #*mul(970,745)!#?@(who(641,375)mul(338,404) ){mul(546,582)'*!mul(491,915);why(807,382)mul(737,259)mul(769,95):what()/?+select()%why(){mul(219,377)mul(290,206)~%[[mul(492,759)?mul(982,630)&}+$@mul(722,843) :~'+/)mul(924,380)#;;who()select()+do()why(196,318)#$*when(747,804)~mul(50,493)>where()~]}#mul(183,580)mul(970,128)[select()}@;where()[why()mul(174,357)~](+[~#mul(471,870)^'from(874,759)%don't()when()[where()who()(mul(880,149)+@?mul(319,427)&&~from()<mul(996,58) ~^)where())!^mul(168,373)who()@where()how()*?(!*]mul(978,658)~]who()]$&how()why()<]mul(575,451)'/*mul(365,231)(~where()$&,(/where()<don't()select()[what()@/{+(from()mul(323,211)why()select()when()${mul(799,599)#'/'(from()+@mul(75,724)[::>$(mul(186,123)%what() }*(do()when()-where()!/)(mul(810,752)mul(421,178);{# !when()%mul(926,537)when()'mul(697,480){:~#]{<who()mul(371,502)!)/!what()how()  {mul(452,449)from(),mul(117,131);when()$mul(602,113)(how()(}}when()>>-mul(536,791)*]$~*where()$mul(367,981)?(+~#mul(982,905)><},,*where() where()@mul(321,839)!{->]?what(){mul(467,883):/+)mul(849,445)why()when()[&<mul(558,491)what()%&*}*)mul(58,503)why()where()!why()+,mul(972,943)who()select()what()why()from()mul(552,996)}}from(88,271)&what()^/mul(252,989)](%{mul(193,149)&from()!mul(19,790)-who(),{!mul(842,509) *><do(),why()mul(834,147)/what()@<what()*(mul(334,354)'what()>$+!#
"""

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, raw_string)

if matches:
    print(f"WE HAVE MATCHES, LEN: {len(matches)}")
    
sum = 0

for match in matches:
    x = int(match[0])
    y = int(match[1])
    sum += (x * y)

print(sum)

