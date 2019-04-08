"""
Autor: Michael McHugh
Fecha: 12-15 Noviembre
Obtenido de: https://github.com/mmchugh/pynoise
"""
vectors = (
    (-0.930880565725712, -0.3460180084878941, -0.1171875),
    (0.2393344521679812, 0.9080500853507214, 0.34375),
    (0.8735766900760917, -0.30053012561047826, -0.3828125),
    (0.517481464184992, -0.8398192843217562, -0.1640625),
    (0.9308805657257119, -0.3460180084878944, 0.1171875),
    (-0.1630459077890721, -0.4077083400508106, -0.8984375),
    (0.8766014519841998, 0.3015707120713028, 0.375),
    (0.4736258605128182, 0.10026736385032023, -0.875),
    (-0.9574051394386797, -0.1300312032558038, 0.2578125),
    (0.41459550859014793, 0.9051637983022058, -0.09375),
    (-0.5422772678450828, -0.6444741933330009, 0.5390625),
    (0.8643956417489136, 0.05310531541647927, -0.5),
    (-0.3475363640335912, -0.506555867371074, 0.7890625),
    (-0.5167831411892694, 0.8386859777995287, -0.171875),
    (0.6802685919158965, 0.7322964429469554, 0.03125),
    (0.3992497525674504, -0.8180170421015566, -0.4140625),
    (-0.2385961606755218, -0.9052489606205857, 0.3515625),
    (-0.474274887789376, -0.8137624511527457, -0.3359375),
    (0.29725617337080906, 0.8640600123214495, -0.40625),
    (0.9073905268780329, 0.41561542528160056, 0.0625),
    (-0.35713642941192264, 0.6488740672595128, -0.671875),
    (0.4807035618873847, 0.3297996900980674, -0.8125),
    (-0.48718421254451566, -0.10313768899451947, -0.8671875),
    (-0.12945180702960088, -0.9531391101253379, -0.2734375),
    (-0.8536549600702169, 0.07351236986056396, -0.515625),
    (-0.9063891759823655, 0.4151567728425114, -0.078125),
    (0.10857878017140143, -0.5128859104033182, -0.8515625),
    (0.11425684057265936, 0.613672397849499, -0.78125),
    (0.9993223845883495, 0.03680722294135883, 0.0),
    (0.12474622662084037, -0.001530943373197193, 0.9921875),
    (0.0030438223601458934, 0.24802050851782373, 0.96875),
    (0.48718421254451566, -0.10313768899451944, 0.8671875),
    (-0.23344707987602656, -0.22778660680800805, 0.9453125),
    (-0.3463283625979503, 0.9317155009095978, -0.109375),
    (0.7338980279480395, 0.38077215572305, 0.5625),
    (0.7441742892341304, 0.23575331862537344, -0.625),
    (0.7291318723216247, -0.3782993062490492, -0.5703125),
    (0.002641252523330256, -0.2152178138046616, -0.9765625),
    (0.7559796094316105, 0.5751856918627496, -0.3125),
    (-0.33855487593698336, -0.14512666303282734, -0.9296875),
    (-0.29837313135297844, -0.8673067698803971, -0.3984375),
    (0.3531401271805121, 0.5147237007122674, 0.78125),
    (0.11602396398782978, -0.6231636008098521, 0.7734375),
    (0.2430089585705776, 0.7670772995953167, 0.59375),
    (0.5796619126163641, -0.7618628079619642, -0.2890625),
    (0.12914829539928557, 0.9509043880934923, -0.28125),
    (-0.002641252523330335, -0.2152178138046616, 0.9765625),
    (-0.2120280977705615, -0.7311449202104513, -0.6484375),
    (-0.6425989980297371, -0.35368266860976927, -0.6796875),
    (0.585132309471803, 0.6617353080440805, -0.46875),
    (-0.9632717817673865, 0.22876206815310185, -0.140625),
    (0.0757337206281652, -0.6829138577841023, -0.7265625),
    (0.07663404065411634, 0.6910323156792476, 0.71875),
    (-0.955305873438747, 0.12974608875967203, -0.265625),
    (-0.8161384049714355, 0.475659634934142, -0.328125),
    (0.7500765496374724, -0.23762314602684328, 0.6171875),
    (-0.19328642549120473, -0.1980895727053369, -0.9609375),
    (-0.9598013854929545, 0.15443335061056296, 0.234375),
    (-0.15472729612006086, -0.9616282532398499, 0.2265625),
    (0.21202809777056122, -0.7311449202104514, 0.6484375),
    (-0.17607154847511297, 0.002160831454772818, 0.984375),
    (0.9992918872240457, -0.036806099656917494, -0.0078125),
    (-0.23945512747293612, 0.7558593462423547, -0.609375),
    (-0.539024955369309, 0.6406089539368885, -0.546875),
    (-0.29946435532604854, 0.8704787241881068, 0.390625),
    (0.24906378639963536, 0.24302464958163564, 0.9375),
    (-0.5726171423073948, -0.79222154693587, -0.2109375),
    (0.5422772678450826, -0.6444741933330012, -0.5390625),
    (-0.7436662195838551, -0.21565920730079513, 0.6328125),
    (0.5810693056254347, 0.7637125765364711, 0.28125),
    (0.8582910574156762, -0.07391160669360601, -0.5078125),
    (0.40079083812456573, 0.8211745500046919, 0.40625),
    (-0.8386859777995287, 0.5167831411892696, 0.171875),
    (-0.9579089267786101, -0.15412885142503774, -0.2421875),
    (0.34688416429048313, 0.9332107554376412, 0.09375),
    (-0.724267961009785, 0.37577573768103845, -0.578125),
    (0.818451798188558, -0.47700792067392966, -0.3203125),
    (-0.5735856209258601, 0.793561446796715, 0.203125),
    (0.37057227774377727, 0.7142388427324495, -0.59375),
    (0.36382864512110025, 0.6610330207253982, 0.65625),
    (-0.22849839825186938, -0.962161520011105, -0.1484375),
    (-0.07481265714505529, 0.6746083498637535, -0.734375),
    (0.6574076672399921, 0.07290513736405604, -0.75),
    (0.48955751443135326, -0.335874183895615, 0.8046875),
    (-0.5174814641849922, -0.839819284321756, 0.1640625),
    (0.6425989980297372, -0.35368266860976927, 0.6796875),
    (0.16655704774307523, 0.38854817892651483, 0.90625),
    (0.22849839825186902, -0.9621615200111051, 0.1484375),
    (-0.7318489110082256, 0.6798528560145014, 0.046875),
    (0.19328642549120456, -0.19808957270533706, 0.9609375),
    (0.15979267343749484, -0.3727680882391197, -0.9140625),
    (-0.6366641249624194, -0.5357056741622089, -0.5546875),
    (0.3605177483264027, -0.6550175182660465, -0.6640625),
    (-0.7558593462423547, 0.23945512747293607, 0.609375),
    (-0.47565963493414176, 0.8161384049714356, 0.328125),
    (-0.8994302107156156, -0.23706251474202628, -0.3671875),
    (0.6361884159242198, 0.35015432232635907, -0.6875),
    (-0.9643208528635641, -0.2290112062241462, 0.1328125),
    (0.03678924627462549, 0.9988343150185346, -0.03125),
    (-0.5796619126163645, -0.7618628079619639, 0.2890625),
    (-0.9317155009095976, 0.3463283625979507, 0.109375),
    (-0.05390954852242203, -0.8774861504159815, 0.4765625),
    (-0.6746083498637535, 0.07481265714505542, 0.734375),
    (-0.7374703185299403, 0.21386242929123464, -0.640625),
    (0.2926957581185117, 0.4499056908724645, -0.84375),
    (0.34753636403359106, -0.5065558673710742, -0.7890625),
    (0.8207031598406468, 0.4783200533404155, 0.3125),
    (-0.44431650289024316, 0.555155905700718, 0.703125),
    (0.4728533589089715, 0.8113233871080652, -0.34375),
    (0.9559504875530878, 0.15381373588536904, -0.25),
    (-0.667815383322976, 0.5905085504649249, -0.453125),
    (0.7579967502000822, -0.5767204296969757, 0.3046875),
    (0.43943568198051813, -0.5490575129219769, 0.7109375),
    (-0.8732140912967051, 0.0536470887921203, 0.484375),
    (0.5726171423073945, -0.7922215469358702, 0.2109375),
    (-0.07351236986056361, 0.8536549600702169, 0.515625),
    (-0.3992497525674507, -0.8180170421015563, 0.4140625),
    (-0.6798528560145012, 0.7318489110082257, -0.046875),
    (-0.43943568198051836, -0.5490575129219768, -0.7109375),
    (0.4886524725233586, 0.3179033046333561, 0.8125),
    (0.9574051394386797, -0.13003120325580417, -0.2578125),
    (-0.5611217325483167, -0.4490912252602196, 0.6953125),
    (0.794848651935977, -0.5745160118389306, -0.1953125),
    (-0.07310480736316363, -0.848922181789441, -0.5234375),
    (-0.2113124674490429, 0.216563559897775, 0.953125),
    (0.6326382175638526, 0.5323181714704387, -0.5625),
    (0.862832032261119, 0.07430265206671316, 0.5),
    (0.21015522938811276, 0.7246866336982004, -0.65625),
    (-0.6406089539368884, 0.5390249553693091, 0.546875),
    (0.07310480736316331, -0.848922181789441, 0.5234375),
    (-0.8688510476524056, -0.05337903930446003, -0.4921875),
    (-0.0368027295978835, 0.9992003895461337, 0.015625),
    (-0.3732004211380638, -0.7193043109533835, -0.5859375),
    (-0.8114829650814545, -0.3960606641997676, -0.4296875),
    (0.3385548759369833, -0.14512666303282745, 0.9296875),
    (-0.9069178045084252, -0.4153989025134371, 0.0703125),
    (0.7960834179635301, 0.5754084998012312, 0.1875),
    (-0.7579967502000824, -0.5767204296969755, -0.3046875),
    (0.2334470798760266, -0.22778660680800802, -0.9453125),
    (-0.1544333506105628, 0.9598013854929545, -0.234375),
    (-0.6800815422101704, -0.7320950874297589, 0.0390625),
    (-0.15266695082549295, 0.35614503576583306, -0.921875),
    (0.1547272961200605, -0.96162825323985, -0.2265625),
    (-0.5878493563667291, -0.664808059001222, -0.4609375),
    (0.5716103823877392, 0.7908286845117231, -0.21875),
    (-0.5002585572153637, 0.10590554899438746, 0.859375),
    (0.9594373511812079, 0.13030721069222362, 0.25),
    (0.7312219061348977, 0.6792703982866078, -0.0625),
    (0.6707581610250576, -0.5931106699107958, -0.4453125),
    (-0.4793937479066713, -0.3118798435483526, 0.8203125),
    (0.8964111802024919, 0.2362667898964549, -0.375),
    (-0.11602396398783, -0.6231636008098521, -0.7734375),
    (-0.8735766900760918, -0.30053012561047787, 0.3828125),
    (0.9643208528635641, -0.2290112062241461, -0.1328125),
    (-0.3976731692304124, 0.8147868033106818, -0.421875),
    (-0.8374983170982427, -0.5160513261308038, -0.1796875),
    (-0.7935614467967149, 0.5735856209258602, -0.203125),
    (0.44951107331563595, 0.17976316354199204, 0.875),
    (0.1569714342230826, 0.3925186700501626, -0.90625),
    (0.7315578684343307, -0.6795824912956252, 0.0546875),
    (-0.7291318723216247, -0.37829930624904934, 0.5703125),
    (-0.22876206815310166, 0.9632717817673866, 0.140625),
    (0.8994302107156156, -0.23706251474202622, 0.3671875),
    (0.23859616067552145, -0.9052489606205858, -0.3515625),
    (-0.5905085504649248, 0.6678153833229761, 0.453125),
    (-0.0021608314547727856, 0.17607154847511297, -0.984375),
    (0.11116420952020123, 0.5250985203004754, 0.84375),
    (-0.6414491833385348, -0.11942847247652721, 0.7578125),
    (0.054166499749680984, 0.8816685475873957, 0.46875),
    (0.5181464305330535, 0.8408984564297021, 0.15625),
    (-0.5551559057007179, 0.4443165028902432, -0.703125),
    (0.9653089328006179, 0.22924585984338366, 0.125),
    (-0.9992918872240458, -0.03680609965691668, 0.0078125),
    (-0.21386242929123447, 0.7374703185299404, 0.640625),
    (-0.12474622662084037, -0.001530943373197092, -0.9921875),
    (-0.8147868033106818, 0.39767316923041257, 0.421875),
    (-0.6707581610250575, -0.5931106699107958, 0.4453125),
    (-0.3417836015958749, 0.49817085829577806, -0.796875),
    (-0.03679711214694719, -0.999047874794494, -0.0234375),
    (-0.43614302687845496, -0.17441717217364025, 0.8828125),
    (0.4361430268784549, -0.17441717217364044, -0.8828125),
    (0.8362560706345985, 0.5152858763121513, -0.1875),
    (-0.48955751443135337, -0.33587418389561485, -0.8046875),
    (0.47427488778937577, -0.8137624511527458, 0.3359375),
    (0.0, 0.0, -1.0),
    (-0.7500765496374726, -0.23762314602684267, -0.6171875),
    (0.9069178045084251, -0.4153989025134374, -0.0703125),
    (0.17322467601470265, 0.17752929087787542, -0.96875),
    (0.8688510476524056, -0.05337903930446074, 0.4921875),
    (-0.8704787241881066, 0.2994643553260489, -0.390625),
    (-0.9023758988648496, 0.2378389087656913, 0.359375),
    (0.346617063177272, -0.9324921823308295, -0.1015625),
    (0.8114829650814542, -0.3960606641997679, 0.4296875),
    (-0.12974608875967186, 0.955305873438747, 0.265625),
    (0.8374983170982423, -0.5160513261308045, 0.1796875),
    (-0.24125012513786262, -0.7615254005709302, 0.6015625),
    (-0.3056783625599803, 0.46986138704691327, 0.828125),
    (0.6502631580714835, 0.12106950588360749, 0.75),
    (0.6414491833385348, -0.11942847247652745, -0.7578125),
    (0.5611217325483165, -0.4490912252602198, -0.6953125),
    (0.03679711214694682, -0.9990478747944941, 0.0234375),
    (-0.8184517981885583, -0.477007920673929, 0.3203125),
    (0.3732004211380635, -0.7193043109533837, 0.5859375),
    (0.5669591782544728, 0.4537631983678412, 0.6875),
    (0.1294518070296005, -0.9531391101253379, 0.2734375),
    (-0.7948486519359771, -0.5745160118389304, 0.1953125),
    (-0.6488740672595127, 0.3571364294119228, 0.671875),
    (-0.7599576716767358, 0.578212393186686, 0.296875),
    (-0.15979267343749498, -0.3727680882391196, 0.9140625),
    (0.95790892677861, -0.1541288514250381, 0.2421875),
    (0.47939374790667105, -0.3118798435483529, -0.8203125),
    (0.5454638094883225, 0.6482612668041235, 0.53125),
    (-0.42222746839340614, 0.16885222624856083, -0.890625),
    (-0.360517748326403, -0.6550175182660464, 0.6640625),
    (0.4344451866195878, 0.54282208625209, -0.71875),
    (0.053909548522421705, -0.8774861504159815, -0.4765625),
    (0.16304590778907194, -0.40770834005081064, 0.8984375),
    (-0.11774720814634826, 0.6324191287024298, 0.765625),
    (-0.05364708879212034, 0.8732140912967051, -0.484375),
    (0.2983731313529781, -0.8673067698803972, 0.3984375),
    (0.15501074799207035, 0.9633899031580822, 0.21875),
    (-0.41515677284251123, 0.9063891759823656, 0.078125),
    (0.22822014615321645, 0.9609898555082693, -0.15625),
    (0.2412501251378623, -0.7615254005709302, -0.6015625),
    (-0.37577573768103834, 0.7242679610097851, 0.578125),
    (-0.4148889914361757, -0.9058045434191766, -0.0859375),
    (-0.16885222624856075, 0.4222274683934062, 0.890625),
    (-0.35614503576583306, 0.15266695082549303, 0.921875),
    (-0.6324191287024298, 0.11774720814634825, -0.765625),
    (-0.23783890876569114, 0.9023758988648496, -0.359375),
    (0.6736372380218326, 0.5956564626949975, 0.4375),
    (0.9299872198798812, 0.345685942526001, -0.125),
    (0.7497358339188678, 0.217419362840525, 0.625),
    (-0.8582910574156762, -0.0739116066936057, 0.5078125),
    (-0.3466170631772723, -0.9324921823308294, 0.1015625),
    (-0.6661087951453707, -0.07387007427729142, -0.7421875),
    (0.7436662195838549, -0.21565920730079574, -0.6328125),
    (-0.2992877957311759, -0.4600383803772507, -0.8359375),
    (-0.5782123931866858, 0.7599576716767359, -0.296875),
    (0.41488899143617536, -0.9058045434191767, 0.0859375),
    (-0.07573372062816547, -0.6829138577841023, 0.7265625),
    (0.6661087951453707, -0.07387007427729167, 0.7421875),
    (0.6366641249624193, -0.535705674162209, 0.5546875),
    (0.07268877915673755, 0.8440910963188173, -0.53125),
    (0.2992877957311757, -0.46003838037725076, 0.8359375),
    (0.8081046247071149, 0.39441179689123546, -0.4375),
    (-0.21656355989777498, 0.21131246744904292, -0.953125),
    (-0.10590554899438727, 0.5002585572153638, -0.859375),
    (-0.9992003895461337, 0.036802729597883464, -0.015625),
    (0.5878493563667286, -0.6648080590012225, 0.4609375),
    (0.3198380843014588, 0.13710342749316262, -0.9375),
    (-0.498170858295778, 0.34178360159587506, 0.796875),
    (-0.4698613870469132, 0.3056783625599804, -0.828125),
    (-0.10857878017140163, -0.5128859104033181, 0.8515625),
    (-0.7315578684343306, -0.6795824912956252, -0.0546875),
    (0.6800815422101698, -0.7320950874297595, -0.0390625),
)

x_noise = 17909
y_noise = 92921
z_noise = 48163
seed = 1625