
import React from 'react'
import ecom from './images/E-com.png';
import store from './images/bag.png';
import Bi from './images/BI1.jpg';
import './css/Body.css';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function Body() {
    return (
        <div className='body-cont' >
            <div className='body'>
                <div className='row' style={{ width: '75%', margin: ' auto' }}>
                    <h1 style={{ color: '#2F80ED', fontSize: '80px', fontFamily: 'monospace', fontWeight: "bolder", margin: '25px 0px 25px 0px' }}>Auto–BInalysis</h1>

                    <div className='col-sm-12 col-md-12 col-lg-6' style={{ color: 'white' }}>
                        <h1 style={{ fontSize: '60px', fontWeight: 'bolder', fontFamily: 'initial' }}>Remove barriers,<br></br>
                            find clarity,<br></br>
                            exceed goals
                        </h1>
                        <br></br>
                        <p style={{ fontSize: '40px', fontWeight: 'bolder', fontFamily: 'cursive' }}> Lead your way to secure future</p>
                    </div>
                    <div className='col-sm-12 col-md-12 col-lg-6'>

                        <img src={Bi} className="card-img-top busInt" alt="" />
                    </div>

                </div>
                <br></br>
                <br></br>
            </div>
            <div className='details'>

                <div className='row'>
                    <br></br>
                    <br></br>
                    <h4>Group No : C9</h4><br></br>
                    <h3 >F-19 BCSE 117 HAMID FARAZ CH.</h3>
                    <h3>F-19 BCSE 136 MUHAMMAD JUNAID ABBAS</h3>
                    <h3>F-19 BCSE 137 MUHAMMAD SAAD MUBEEN</h3>
                    <br></br>
                    <h4>Supervisor : Dr. Imran Daud</h4>
                    <br></br>
                    <br></br>
                    <br></br>
                    <h2>Purpuse</h2>
                    <p style={{ paddingLeft: '20px', fontSize: '18px', fontStyle: 'italic', textAlign: 'justify' }}>It is increasingly becoming important for business organizations to have a clear view of all their data to stay
                        competitive, which is where business intelligence (BI) tools come in. Nearly 50% of all businesses already use BI tools, and projections show continued growth
                        in coming years.  [2] Similarly in Pakistan, many business organizations have guessed the need to employ BI for their businesses, BUT haven’t yet adopted any
                        tool for it, and the need for such a tool is increasing significantly. So, Auto-BInalysis is a web-based tool that is designed to provide BI to E-Commerce
                        stores and superstores/supermarkets. This system will combine business analytics, data pre-processing, data mining, data visualization, data tools and
                        infrastructure, and reporting by incorporating best Data Science practices to help commerce businesses make more data-driven decisions. As already explained,
                        BI services will be provided to two types of stores i.e., E-Commerce stores and local superstores/supermarkets. Primarily, these services will include Sales
                        Predictions, Sales Analysis, Customer Churn Predictions, Association Mining of goods/products </p>
                </div>
            </div>
            <center>
                <div style={{ background: '#F2F2F2' }}>
                    <div className="row row-card" style={{ width: '60%' }}>
                        <div className="col-sm-12 col-md-12 col-lg-6 E-com-card">
                            <div className="card" style={{ width: '400px', marginTop:' 10px' }}>
                                <div className='E-com'>
                                    <img src={ecom} className="card-img-top ecom" alt="" />
                                </div>
                                <div className="card-body">
                                    <h5 className="card-title">E-Commerce</h5>
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>

                                    {/* <a className="nav-link" style={{ textAlign: 'right' }} href="/">Click to learn more</a> */}
                                    <ul style={{ textAlign: 'left'  , listStyle:'none' }}>
                                       
                                        <li> Data Acquisition</li>
                                        <li> Data Mining</li>
                                        <li> Data Preprocessing</li>
                                        <li> Data Visualization</li>
                                        <li> Customer Churn Prediction</li>
                                        <li> Product Grouping</li>
                                        <li> Sales Analysis</li>
                                        <li> Sales Predictions</li>
                                        <li> Reporting</li>

                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="col-sm-12 col-md-12 col-lg-6 Super-card">
                            <div className="card" style={{ width: ' 400px', marginTop:' 10px' }}>
                                <div className='Store'>
                                    <img src={store} className="card-img-top store" alt="" />
                                </div>

                                <div className="card-body">
                                    <h5 className="card-title">Super Store</h5>
                                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                    {/* <a className="nav-link" style={{ textAlign: 'right' }} href="/">Click to learn more</a> */}
                                    <ul style={{ textAlign: 'left', listStyle:'none' }}>
                                       
                                        <li> Data Acquisition</li>
                                        <li> Data Mining</li>
                                        <li> Data Preprocessing</li>
                                        <li> Data Visualization</li>
                                        <li> Customer Churn Prediction</li>
                                        <li> Product Grouping</li>
                                        <li> Sales Analysis</li>
                                        <li> Sales Predictions</li>
                                        <li> Reporting</li>
                                        
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </center>

        </div>

    )
}

