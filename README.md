# Taiko-Parser
> A simple Parser for Taiko no Tatsujin charts. I did it in less than 5 hours and I'm proud that I finished it, it has chances to improve in the future!

# About Taiko no Tatsujin (or only Taiko)
> Taiko no Tatsujin is a music game series created by Namco. Games have already been released for arcade, Nintendo DS, PlayStation 2, PlayStation Portable, Wii, iPhone OS, Advanced Pico Beena, mobile phone, Android, Nintendo Switch and PlayStation 4.

![Taiko no Tatsujin](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaSLO7NPkIMl_i3g8ISjP8vMWR06ncgwEDdcZrgD0gjJPZMkcLS6EDclc&s=10)

# Why use?
> I don't know, whether you want to make a game like Taiko or want to better understand how the system works.

# How .TJA Chart works
> The chart works using line breaks, each line has some information, like `TITLE:something`. But let's not focus on that, but on that part full of strange numbers, for example:
```xml
TITLE:my chart
AUTHOR:UesleiDev
ARTIST:something
COURSE:3
.......something

#START
001020100200211211,
1425772,
16281717272632200,
.......something
#END
```

> Well, after the `#START` the chart really starts. That bunch of numbers is actually the grade type, the only numbers that aren't grades are `0` and `7`.
