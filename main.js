// ************************************************************************** //
//                                                                            //
//                                                        :::      ::::::::   //
//   main.js                                            :+:      :+:    :+:   //
//                                                    +:+ +:+         +:+     //
//   By: ezanotti <marvin@42.fr>                    +#+  +:+       +#+        //
//                                                +#+#+#+#+#+   +#+           //
//   Created: 2022/12/02 13:35:06 by ezanotti          #+#    #+#             //
//   Updated: 2022/12/02 13:40:58 by ezanotti         ###   ########lyon.fr   //
//                                                                            //
// ************************************************************************** //

var API_KEY = 'NGQyMGI5YTEtZTIzNi00ZDIxLTgwY2ItMjgwMDgyOTcwOTUw';


console.log("fefe");



Napster.init({
	consumerKey: API_KEY,
	version: 'v2.2',
	isHTML5Compatible: true
});


Napster.player.play('Tra.5156528');
