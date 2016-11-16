import { Component,ViewChild} from '@angular/core';
import { Chart,ChartComponent } from 'ng2-chartjs2';
//import { NavController } from 'ionic-angular';
import { APIService } from '../../providers/donation-service'
import { NavController,NavParams } from 'ionic-angular';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html',
  providers: [APIService]
})
export class HomePage {
  @ViewChild(ChartComponent) chartComp;
  labels: string[] =  ["Done","TODO"];
  data: Chart.Dataset[] = [
    {
      label: 'Donation Hours',
      data: [12,60],
      backgroundColor: [
        'rgba(28, 252, 28, 0.2)',
        'rgba(255, 99, 132, 0.2)'
      ],
      borderColor: [
        'rgba(28, 252, 28, 1)',
        'rgba(255, 99, 132, 1)'
      ],
      borderWidth: 1
    }];

    id:string;
    fullname:string;

  constructor(public donationService: APIService,public params:NavParams) {
    console.log('Home: ' + params.get('id'))
    this.id = params.get('id');
    this.getHours();
  }


   loadData(){
     this.updateData([0,60]);
   }

  getHours(){
    this.donationService.getInfo(this.id)
    .then(hours =>{
       this.updateData([hours['mins_done'],hours['minutes_left']])
       this.fullname = hours['first_name'] +' '+hours['last_name'];
       
      
    }); 
  }

updateData(newData){
    let chart = this.chartComp.chart;
    chart.data.datasets[0].data[0] = [0,60];
    chart.update()
  }
  

  getID(){
    alert(this.id)
  }

}
