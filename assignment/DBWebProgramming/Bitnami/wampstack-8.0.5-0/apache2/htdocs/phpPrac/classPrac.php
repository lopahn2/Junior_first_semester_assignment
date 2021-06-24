<?php
class MyCalculator{
    private $_fval, $_sval;
    public function __construct($_fval, $_sval){
        $this->_fval = $_fval;
        $this->_sval = $_sval;
    }
    public function add(){
        return $this->_fval + $this->_sval;
    }
    public function sub(){
        return $this->_fval - $this->_sval;
    }
    public function mul(){
        return $this->_fval * $this->_sval;
    }
    public function div(){
        return $this->_fval / $this->_sval;
    }
}

$mycalc = new MyCalculator(12, 6);
echo $mycalc->add()."\n";
echo $mycalc->sub()."\n";
echo $mycalc->mul()."\n";
echo $mycalc->div()."\n";
?>