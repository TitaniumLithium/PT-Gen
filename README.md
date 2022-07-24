PT-Gen 可根据豆瓣、IMDb、Bangumi、Steam、GOG 链接自动生成简介。

这个工具提取自 Rhilip 开发的 [PT-help](https://github.com/Rhilip/PT-help) ，去掉了源码中与 PT-Gen 不相关的代码和模块。

## 停止维护

2020年8月19日，豆瓣的api_key全部失效，此项目 python 版已无法正常使用，无限期停止维护。

游戏平台的功能仍可使用 2022/07/23 为其添加GOG链接支持

支持GOG链接的demo:  https://ptgen.titaniumlithium.me

GOG regex: `(https?://)?(www\.)?gog\.com/[a-zA-Z]?[a-zA-Z]?/?game/(?P<sid>\S+)`

引入了`html2bbcode3`以代替`html2bbcode`请参照https://github.com/issaccv/html2bbcode3 安装

需要请求豆瓣链接请换用 Rhilip 大佬开发的 cfworker 版本：https://github.com/Rhilip/pt-gen-cfworker

## 演示

https://www.bfdz.ink/tools/ptgen

https://ptgen.titaniumlithium.me

## Wiki

- [接口说明](https://github.com/BFDZ/PT-Gen/wiki/%E6%8E%A5%E5%8F%A3%E8%AF%B4%E6%98%8E)
- [部署说明](https://github.com/BFDZ/PT-Gen/wiki/%E9%83%A8%E7%BD%B2%E8%AF%B4%E6%98%8E)
- [部署说明（Docker）](https://github.com/BFDZ/PT-Gen/wiki/%E9%83%A8%E7%BD%B2%E8%AF%B4%E6%98%8E%EF%BC%88Docker%EF%BC%89)
