# Triangulácia polohy lietadla

Program si nastaví súradnicovú sústavu tak že bod H1 je v bode $[0,0]$, bod H2 $[1.5,\frac{3\sqrt{3}}{2}]$ a bod H3 $[-1.5,\frac{3\sqrt{3}}{2}]$, teda "pod" bodom H1. 

Následne binárne vyhľadáva vzdialenosť R od bodu H1. 
To robí tak že si nastaví horný a dolný limit pre R - $[0,1e6]$ a následne nájde horný prienik kružníc z H2 a H3 pre $R=\frac{up+down}{2}$, kde sú ich polomery zväčšené o $\Delta s_2, \Delta s_3$ ktoré sa spočítajú z $\Delta t_2, \Delta t_3$ a $v$ zvuku vo vode.

Ak je vzdialenosť H1 - prienik menšia ako R tak vieme že musíme zväčšiť R a teda zmeníme down na R, inak zmeníme up na R čím nové R zmenšíme.