
DROP TABLE IF EXISTS accounts;
	CREATE TABLE `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    `major` varchar(100),
    PRIMARY KEY (`id`)
) ;

INSERT INTO `accounts` (`id`, `username`, `password`, `email`, `major`) VALUES (1, 'test', 'test', 'test@test.com', 'Math');