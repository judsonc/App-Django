<?php require_once("../header.php"); ?>

	<div class="container" >
	        	<div class="col-xs-12">
			<div class="col-xs-3">
				<div class="corpo">
				<span class="orelha"></span>
				<div class="menuTexto">

					<h2>Portfolio</h2>
					<hr>
					<a href="#"><p> > Sites </p></a>
					<a href="#"><p> > Programas </p></a>
					<a href="#"><p> > Consultorias </p></a>
					<a href="#"><p> > Eventos </p></a>
				</div>
			</div>
			<span class="bandeira"></span>
			</div>
			<div class="containerImg col-xs-9">
				<div class="col-xs-4 colImg">
					<img src="<?php echo Dbcommand::getServer(); ?>/components/img/s2.png" class="imgPort">
					<img src="<?php echo Dbcommand::getServer();; ?>/components/img/s1.jpeg" class="imgPort">
				</div>
				<div class="col-xs-4 colImg">
					<img src="<?php echo Dbcommand::getServer(); ?>/components/img/s1.png" class="imgPort">
					<img src="<?php echo Dbcommand::getServer(); ?>/components/img/s2.png" class="imgPort">
				</div>
				<div class="col-xs-4 colImg">
					<img src="<?php echo Dbcommand::getServer(); ?>/components/img/s2.png" class="imgPort">
					<img src="<?php echo Dbcommand::getServer(); ?>/components/img/s1.png" class="imgPort">
				</div>
			</div>
		</div>
	</div>
<?php include("../footer.php"); ?>
