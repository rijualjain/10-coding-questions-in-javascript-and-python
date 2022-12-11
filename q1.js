function exercise1(SepalLen,SepalWid,PetalLen,PetalWid){
    if(PetalLen<2.5){
        return 'setosa';
    }
    else{
        if(PetalWid<1.8){
            if(PetalLen<5){
                if(PetalWid<1.7){
                    return 'versicol';
                }
                else{
                    return 'virginic';
                }
            }
            else{
                if(PetalWid>=1.6){
                    if(SepalLen<7){
                        return 'versicol';
                    }
                    else{
                        return 'virginic';                    
                    }
                }
                else{
                    return 'virginic';
                }
            }
        }
        else{
            if(PetalLen<4.9){
                if(SepalLen<6){
                    return 'versicol';
                }
                else{
                    return 'virginic';
                }
            }
            else{
                return 'virginic';
            }
        }
    }
}

