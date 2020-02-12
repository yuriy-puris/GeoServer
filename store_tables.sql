CREATE TABLE shop (
  [name] VARCHAR(255) NOT NULL,
  [url] VARCHAR(255) NOT NULL,
  search_request VARCHAR(255) NOT NULL,

  PRIMARY KEY (id)
);

CREATE TABLE [address] (
  shop_address VARCHAR(255) NOT NULL,
  shop_id INT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (shop_id) REFERENCES [shop](id)  
);

CREATE TABLE coordinates (
  lat FLOAT,
  lng FLOAT,
  address_id INT NOT NULL,

  PRIMARY KEY (id),
  FOREIGN KEY (address_id) REFERENCES [address](id)
);