# -*- coding: utf-8 -*-
import nysol._nysolshell_core as n_core
from nysol.mcmd.nysollib.core import NysolMOD_CORE
from nysol.mcmd.nysollib import nysolutil as nutil

class Nysol_Msetstr(NysolMOD_CORE):

	_kwd ,_inkwd ,_outkwd = n_core.getparalist("msetstr",3)

	def __init__(self,*args, **kw_args) :
		super(Nysol_Msetstr,self).__init__("msetstr",nutil.args2dict(args,kw_args,Nysol_Msetstr._kwd))

def msetstr(self,*args, **kw_args):
	return Nysol_Msetstr(nutil.args2dict(args,kw_args,Nysol_Msetstr._kwd)).addPre(self)

setattr(NysolMOD_CORE, "msetstr", msetstr)
