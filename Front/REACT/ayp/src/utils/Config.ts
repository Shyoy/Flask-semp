
class Config {
    public supportEmail = "support@northwind.com";
    public supportPhone = "031234567";
    public supportPage = "";
    
 
    public todosUrl = "";
    public registerUrl = "";
    public loginUrl = "";
    
}


class DevelopmentConfig extends Config {
    

    public todosUrl = "http://localhost:5000/todos/";
   
    public registerUrl = "http://localhost:5000/signup";
    public loginUrl = "http://localhost:5000/login";
}

// class TestConfig extends Config {
//     public supportPage = "http://northwnd.com/qa-support/";

//     public productsUrl = "http://localhost:3030/api/products/";
//     public productImagesUrl = "http://localhost:3030/api/products/images/";
// }

// class ProductionConfig extends Config {
//     public supportPage = "http://northwnd.com/support/";

//     public productsUrl = "http://localhost:3030/api/products/";
//     public productImagesUrl = "http://localhost:3030/api/products/images/";
// }


let config = new DevelopmentConfig();

// if (process.env.NODE_ENV === "development") {
//     config = new DevelopmentConfig();
// }
// else if (process.env.NODE_ENV === "test") {
//     config = new TestConfig();
// }
// else if(process.env.NODE_ENV === "production") { 
//     config = new ProductionConfig();
// // }

export default config;