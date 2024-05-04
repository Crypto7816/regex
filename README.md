## 项目说明
- 数据说明：包含`data.csv`和`base_asset_list.pkl`两个文件，
第一文件包含需要处理的文本数据，第二个文件包含需要输出的的基础资产类别，也就是说
第一个文件的文本内容中的资产一定出现在第二个中。第一个文件为`csv`格式，包含`Date`,`Content`,`Coin`三个字段，
第二个文件为`list`格式。
- 项目要求，将`Content`中的coin提取出来，也就是输入为`content`，输出为`coin`。识别率尽可能高，识别速度尽可能快，请避免大量的if语句和无效条件。
- 输入为
```text
🚨🚨

#TroiaRobot Yeni Setup

Spot olarak 0,077$’dan #IOTX satın aldım.

Kısa vade %100’lük bir mum istiyorum. Orta vade ise 0,250$ hedefim.
```
输出为：`IOTX`