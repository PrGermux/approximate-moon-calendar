# Approximate moon calendar
#### An approximate moon calendar, which outputs the year on certain day, when will be next full and new moon

<b>Motivation</b>: Every month we are spectating each phase of Moon, but mostly exciting of them are actually full and new moon. My program calculate the approximate dates, when we can see these phenomena.

<b>Algorithm</b>: As we know Greogrian calendar based on Moon phases on Earth, that means we can predict any phase of the Moon due to date on the Earth. The exact result needs deep astrophysical calculations, because of pertubations of the Moon, gravitation influence from other planets, change of speed of Earth and Moon and other stuff, which are neglected in this code. The approximate moon period is about **29.53 days**, the avarege days pro month is **30.44 days**. So, its clearly seen that the differene between these numbers is about **0.91** day, which means each month any loonar phase moves back **1 day**. 
For instance: ***12.11.2019*** - full moon, the next month ***12-1.11+1.2019*** = ***11.12.2019*** - full moon.
