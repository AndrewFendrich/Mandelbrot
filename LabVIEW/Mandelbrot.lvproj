<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="15008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Calculations" Type="Folder">
			<Item Name="Iterate.vi" Type="VI" URL="../Iterate.vi"/>
		</Item>
		<Item Name="Classes" Type="Folder" URL="../Classes">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="Display" Type="Folder">
			<Item Name="MandelPoint to Pixel.vi" Type="VI" URL="../MandelPoint to Pixel.vi"/>
			<Item Name="Map Iteration to Color.vi" Type="VI" URL="../Map Iteration to Color.vi"/>
			<Item Name="The Grid.vi" Type="VI" URL="../The Grid.vi"/>
		</Item>
		<Item Name="Gradient" Type="Folder">
			<Item Name="Create Gradient Array.vi" Type="VI" URL="../Gradient/Create Gradient Array.vi"/>
			<Item Name="Create Gradient Color Ramp V2.vi" Type="VI" URL="../Gradient/Create Gradient Color Ramp V2.vi"/>
			<Item Name="Create Gradient Color Ramp.vi" Type="VI" URL="../Gradient/Create Gradient Color Ramp.vi"/>
			<Item Name="Scrolling Gradient Color Ramp.vi" Type="VI" URL="../Gradient/Scrolling Gradient Color Ramp.vi"/>
		</Item>
		<Item Name="SubVIs" Type="Folder">
			<Item Name="Create Grid.vi" Type="VI" URL="../Create Grid.vi"/>
		</Item>
		<Item Name="Workbench" Type="Folder">
			<Item Name="rotate colors.vi" Type="VI" URL="../rotate colors.vi"/>
		</Item>
		<Item Name="Bounding Coordinates.ctl" Type="VI" URL="../Bounding Coordinates.ctl"/>
		<Item Name="MandelPoint.ctl" Type="VI" URL="../MandelPoint.ctl"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Color to RGB.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/colorconv.llb/Color to RGB.vi"/>
				<Item Name="Draw Flattened Pixmap.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Draw Flattened Pixmap.vi"/>
				<Item Name="FixBadRect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/pictutil.llb/FixBadRect.vi"/>
				<Item Name="imagedata.ctl" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/imagedata.ctl"/>
				<Item Name="RGB to Color.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/colorconv.llb/RGB to Color.vi"/>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
