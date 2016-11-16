import { Component } from '@angular/core';
import { BarcodeScanner } from 'ionic-native';
import { NavController } from 'ionic-angular';

@Component({
  selector: 'page-contact',
  templateUrl: 'donate.html'
})
export class DonatePage {

  constructor(public navCtrl: NavController) {
      
  }

  donateScan() : void{
      var code = this.scanCode();
      alert(code);
  }

  scanCode(): any {
    BarcodeScanner.scan().then((barcodeData) => {
       return barcodeData;
    }, (err) => {
    // An error occurred
  });
  }
}
