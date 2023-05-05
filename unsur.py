import streamlit as st
from PIL import Image
image = Image.open('D:\kelompok 8\science.jpg')

st.image(image, caption=' ')

import streamlit as st

st.title("Aplikasi Mengetahui Atom Relatif Unsur")
unsur = st.text_input('Masukkan nama unsur')
tombol = st.button('Tampilkan nilai Atom Relatif')


#Percabangan lebih dari dua kasus
if unsur == "H" :
    st.success ("1")
elif unsur == "Li" :
    st.success ("7")
elif unsur == "Na" :
    st.success ("23")
elif unsur == "K" :
    st.success ("39")
elif unsur == "Rb" :
    st.success ("85,5")
elif unsur == "Cs" :
    st.success ("133")
elif unsur == "Fr" :
    st.success ("223")
elif unsur == "Be" :
    st.success ("9")
elif unsur == "Mg" :
    st.success ("24,3")
elif unsur == "Ca" :
    st.success ("40")
elif unsur == "Sr" :
    st.success ("88")
elif unsur == "Ba" :
    st.success ("137")
elif unsur == "Ra" :
    st.success ("226")
elif unsur == "Ra" :
    st.success ("226")
elif unsur == "Sc" :
    st.success ("45")
elif unsur == "Y" :
    st.success ("89")
elif unsur == "Ti" :
    st.success ("48")
elif unsur == "Zr" :
    st.success ("91,2")
elif unsur == "Hf" :
    st.success ("178,5")
elif unsur == "Rf" :
    st.success ("267,1")
elif unsur == "B" :
    st.success ("11")
elif unsur == "Al" :
    st.success ("27")
elif unsur == "Ga" :
    st.success ("70")
elif unsur == "In" :
    st.success ("115")
elif unsur == "Tl" :
    st.success ("204,4")
elif unsur == "Uut" :
    st.success ("Tidak diketahui")
elif unsur == "C" :
    st.success ("12")
elif unsur == "Si" :
    st.success ("28,1")
elif unsur == "Ge" :
    st.success ("73")
elif unsur == "Sn" :
    st.success ("119")
elif unsur == "Pb" :
    st.success ("207,2")
elif unsur == "Fl" :
    st.success ("289,2")
elif unsur == "Nh" :
    st.success ("286,2")
elif unsur == "Lu" :
    st.success ("175")
elif unsur == "Lr" :
    st.success ("262,1")
elif unsur == "V" :
    st.success ("51")
elif unsur == "Nb" :
    st.success ("93")
elif unsur == "Ta" :
    st.success ("181")
elif unsur == "Db" :
    st.success ("262")
elif unsur == "Cr" :
    st.success ("52")
elif unsur == "Mo" :
    st.success ("96")
elif unsur == "W" :
    st.success ("184")
elif unsur == "Sg" :
    st.success ("266")
elif unsur == "N" :
    st.success ("14")
elif unsur == "P" :
    st.success ("31")
elif unsur == "As" :
    st.success ("75")
elif unsur == "Sb" :
    st.success ("122")
elif unsur == "Bi" :
    st.success ("209")
elif unsur == "Uup" :
    st.success ("Tidak diketahui")
elif unsur == "Mc" :
    st.success ("289,2")
elif unsur == "O" :
    st.success ("16")
elif unsur == "S" :
    st.success ("32")
elif unsur == "Se" :
    st.success ("79")
elif unsur == "Te" :
    st.success ("128")
elif unsur == "Po" :
    st.success ("209")
elif unsur == "Lv" :
    st.success ("293.2")
elif unsur == "Mn" :
    st.success ("55")
elif unsur == "Tc" :
    st.success ("99")
elif unsur == "Re" :
    st.success ("186,2")
elif unsur == "Bh" :
    st.success ("264")
elif unsur == "Fe" :
    st.success ("56")
elif unsur == "Ru" :
    st.success ("101")
elif unsur == "Os" :
    st.success ("190,2")
elif unsur == "Hs" :
    st.success ("269")
elif unsur == "Co" :
    st.success ("59")
elif unsur == "Rh" :
    st.success ("103")
elif unsur == "Ir" :
    st.success ("192,2")
elif unsur == "Mt" :
    st.success ("268")
elif unsur == "Ni" :
    st.success ("59")
elif unsur == "Pd" :
    st.success ("106,4")
elif unsur == "Pt" :
    st.success ("195")
elif unsur == "Ds" :
    st.success ("269")
elif unsur == "F" :
    st.success ("19")
elif unsur == "Cl" :
    st.success ("35,5")
elif unsur == "Br" :
    st.success ("80")
elif unsur == "I" :
    st.success ("127")
elif unsur == "At" :
    st.success ("210")
elif unsur == "UUs" :
    st.success ("Tidak diketahui")
elif unsur == "He" :
    st.success ("4")
elif unsur == "Ne" :
    st.success ("20,2")
elif unsur == "Ar" :
    st.success ("40")
elif unsur == "Kr" :
    st.success ("85")
elif unsur == "Xe" :
    st.success ("131,3")
elif unsur == "Rn" :
    st.success ("222")
elif unsur == "UUo" :
    st.success ("Tidak diketahui")
elif unsur == "La" :
    st.success ("139")
elif unsur == "Ce" :
    st.success ("140")
elif unsur == "Pr" :
    st.success ("141")
elif unsur == "Nd" :
    st.success ("144")
elif unsur == "Pm" :
    st.success ("145")
elif unsur == "Sm" :
    st.success ("150")
elif unsur == "Eu" :
    st.success ("152")
elif unsur == "Gd" :
    st.success ("157")
elif unsur == "Td" :
    st.success ("159")
elif unsur == "Dy" :
    st.success ("162")
elif unsur == "Ho" :
    st.success ("165")
elif unsur == "Er" :
    st.success ("167")
elif unsur == "Tm" :
    st.success ("169")
elif unsur == "Yb" :
    st.success ("173")
elif unsur == "Lu" :
    st.success ("175")
elif unsur == "Ac" :
    st.success ("227")
elif unsur == "Th" :
    st.success ("232")
elif unsur == "Pa" :
    st.success ("231")
elif unsur == "U" :
    st.success ("238")
elif unsur == "Np" :
    st.success ("237")
elif unsur == "Pu" :
    st.success ("244")
elif unsur == "Am" :
    st.success ("243")
elif unsur == "Cm" :
    st.success ("247")
elif unsur == "Bk" :
    st.success ("247")
elif unsur == "Cf" :
    st.success ("251")
elif unsur == "Es" :
    st.success ("254")
elif unsur == "Fm" :
    st.success ("257")
elif unsur == "Md" :
    st.success ("258")
elif unsur == "No" :
    st.success ("259")
elif unsur == "Lr" :
    st.success ("262")
else :
    st.success (" ")



    
   
    

    

   

