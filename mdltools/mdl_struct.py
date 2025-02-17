from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()

from .common_struct import *  # NOQA: #402
from construct import *	 # NOQA: #402


mstudiobbox_t = Struct(
    'bone' / Int32sl,
    'group' / Int32sl,
    'bbmin' / Vector,
    'bbmax' / Vector,
    'szhitboxnameindex' / Int32sl,
    'unused' / Int32sl[8],
    # todo: parse 'name'
)

mstudiohitboxset_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'numhitboxes' / Int32sl,
    'hitboxindex' / Int32sl,

    'hitboxes' / Pointer(this.hitboxindex + this._.hitboxsetindex +
                         (this.i*12), mstudiobbox_t[this.numhitboxes]),
    'name' / Pointer(this.sznameindex + this._.hitboxsetindex +
                     (this.i*12), CString('ascii'))
)

mstudiocdtexture_t = Struct(
    'nameoffset' / Int32sl,

    'name' / Pointer(this.nameoffset, CString('ascii'))
)

mstudiotexture_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'flags' / Int32sl,
    'used' / Int32sl,
    'unused1' / Int32sl,
    'unused' / Int32sl[12],

    'name' / Pointer(this.sznameindex + this._.textureindex +
                     (this.i*64), CString('ascii'))
)

mstudiomesh_t = Struct(
    'material' / Int32sl,
    'modelindex' / Int32sl,
    'numvertices' / Int32sl,
    'vertexoffset' / Int32sl,
    'numflexes' / Int32sl,
    'flexindex' / Int32sl,
    'materialtype' / Int32sl,
    'materialparam' / Int32sl,
    'meshid' / Int32sl,
    'center' / Float32l[3],
    'numLODVertexes' / Int32sl,  # ???
    'unused' / Int32sl[8],
)

mstudioeyeball_t = Struct(
    'sznameindex' / Int32sl,
    'bone' / Int32sl,
    'org' / Vector,
    'zoffset' / Float32l,
    'radius' / Float32l,
    'up' / Vector,
    'forward' / Vector,
    'texture' / Int32sl,
    'unused1' / Int32sl,
    'iris_scale' / Float32l,
    'unused2' / Int32sl,
    'upperflexdesc' / Int32sl[3],
    'lowerflexdesc' / Int32sl[3],
    'uppertarget' / Float32l[3],
    'lowertarget' / Float32l[3],
    'upperlidflexdesc' / Int32sl,
    'lowerlidflexdesc' / Int32sl,
    'unused' / Int32sl[4],
    'm_bNonFACS' / Flag,
    'unused3' / Int32sl[3],  # actually char?
    'unused4' / Int32sl[7],
)

mstudiomodel_t = Struct(
    'i' / Index,
    'name' / PaddedString(64, "ascii"),
    'type' / Int32sl,
    'boundingradius' / Float32l,
    'nummeshes' / Int32sl,
    'meshindex' / Int32sl,

    'numvertices' / Int32sl,
    'vertexindex' / Int32sl,
    'tangentsindex' / Int32sl,
    'numattachments' / Int32sl,
    'attachmentindex' / Int32sl,
    'numeyeballs' / Int32sl,
    'eyeballindex' / Int32sl,
    'unused' / Int32sl[10],

    'meshes' / Pointer(this.meshindex + (this.i*148) +
                       this._.modelindex + (this._.i*16) +
                       this._._.bodypartindex, mstudiomesh_t[this.nummeshes]),
    # todo: parse 'mstudioeyeball_t'
)

mstudiobodyparts_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'nummodels' / Int32sl,
    'base' / Int32sl,
    'modelindex' / Int32sl,

    'name' / Pointer(this.sznameindex + this._.bodypartindex +
                     (this.i*16), CString('ascii')),
    'models' / Pointer(this.modelindex + this._.bodypartindex +
                       (this.i*16), mstudiomodel_t[this.nummodels]),
)

mstudiomouth_t = Struct(
    'bone' / Int32sl,
    'forward' / Vector,
    'flexdesc' / Int32sl,
)

mstudioposeparamdesc_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'flags' / Int32sl,
    'start' / Float32l,
    'end' / Float32l,
    'loop' / Float32l,

    'name' / Pointer(this.sznameindex + this._.localposeparamindex +
                     (this.i*20), CString('ascii')),

)

mstudiomovement_t = Struct(
    'endframe' / Int32sl,
    'motionflags' / Int32sl,
    'v0' / Float32l,
    'v1' / Float32l,
    'angle' / Float32l,
    'vector' / Vector,
    'position' / Vector,
)

studioseqdesc_t = Struct(
    'baseptr' / Int32sl,
    'szlabelindex' / Int32sl,  # todo?
    'szactivitynameindex' / Int32sl,
    'flags' / Int32sl,
    'activity' / Int32sl,
    'actweight' / Int32sl,
    'numevents' / Int32sl,
    'eventindex' / Int32sl,
    'bbmin' / Vector,
    'bbmax' / Vector,
    'numblends' / Int32sl,
    'animindexindex' / Int32sl,
    'movementindex' / Int32sl,
    'groupsize' / Int32sl[2],
    'paramindex' / Int32sl[2],
    'paramstart' / Float32l[2],
    'paramend' / Float32l[2],
    'paramparent' / Int32sl,
    'fadeintime' / Float32l[2],
    'fadeouttime' / Float32l[2],
    'localentrynode' / Int32sl,
    'localexitnode' / Int32sl,
    'nodeflags' / Int32sl,
    'entryphase' / Float32l,
    'exitphase' / Float32l,
    'lastframe' / Float32l,
    'nextseq' / Int32sl,
    'pose' / Int32sl,
    'numikrules' / Int32sl,
    'numautolayers' / Int32sl,
    'autolayerindex' / Int32sl,
    'weightlistindex' / Int32sl,
    'posekeyindex' / Int32sl,
    'numiklocks' / Int32sl,
    'iklockindex' / Int32sl,
    'keyvalueindex' / Int32sl,
    'keyvaluesize' / Int32sl,
    'cycleposeindex' / Int32sl,
    'unused' / Int32sl[7],
)

mstudiobone_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'parent' / Int32sl,
    'bonecontroller' / Int32sl[6],
    'pos' / Vector,
    'quat' / Quaternion,
    'rot' / RadianEuler,
    'posscale' / Vector,
    'rotscale' / Vector,
    'poseToBone' / matrix3x4_t,
    'qAlignment' / Quaternion,
    'flags' / Int32sl,
    'proctype' / Int32sl,
    'procindex' / Int32sl,  # todo
    'physicsbone' / Int32sl,
    'surfacepropidx' / Int32sl,
    'contents' / Int32sl,
    'unused' / Int32sl[8],

    'name' / Pointer(this.sznameindex + this._.boneindex +
                     (this.i * 216), CString('ascii')),
    'surfaceprop' / Pointer(this.surfacepropidx + this._.boneindex +
                            (this.i * 216), CString('ascii')),
)

mstudiolinearbone_t = Struct(
    'numbones' / Int32sl,
    'flagsindex' / Int32sl,
    'parentindex' / Int32sl,
    'posindex' / Int32sl,
    'quatindex' / Int32sl,
    'rotindex' / Int32sl,
    'posetoboneindex' / Int32sl,
    'posscaleindex' / Int32sl,
    'rotscaleindex' / Int32sl,
    'qalignmentindex' / Int32sl,
    'unused' / Int32sl[6],
)

mstudiobonecontroller_t = Struct(
    'bone' / Int32sl,
    'type' / Int32sl,
    'start' / Float32l,
    'end' / Float32l,
    'rest' / Int32sl,
    'inputfield' / Int32sl,
    'unused' / Int32sl[8],
)

mstudioflexdesc_t = Struct(
    'szFACSindex' / Int32sl,
)

mstudioflexcontroller_t = Struct(
    'sztypeindex' / Int32sl,
    'sznameindex' / Int32sl,
    'localToGlobal' / Int32sl,
    'min' / Float32l,
    'max' / Float32l,
)

mstudioflexcontrollerui_t = Struct(

    'sznameindex' / Int32sl,
    'szindex0' / Int32sl,
    'szindex1' / Int32sl,
    'szindex2' / Int32sl,
    'remaptype' / Int8ul,
    'stereo' / Flag,
    'unused' / Int8ub[2],
)

mstudioflexrule_t = Struct(
    'flex' / Int32sl,
    'numops' / Int32sl,
    'opindex' / Int32sl,
)

mstudiobbox_t = Struct(
    'bone' / Int32sl,
    'group' / Int32sl,
    'bbmin' / Vector,
    'bbmax' / Vector,
    'szhitboxnameindex' / Int32sl,
    'unused' / Int32sl[8],
)

mstudioevent_t = Struct(
    'cycle' / Float32l,
    'event' / Int32sl,
    'type' / Int32sl,
    'options' / PaddedString(64, "ascii"),
    'szeventindex' / Int32sl,
)

mstudioattachment_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'flags' / Int32ul,
    'localbone' / Int32sl,
    'local' / matrix3x4_t,
    'unused' / Int32sl[8],

    'name' / Pointer(this.sznameindex + this._.localattachmentindex +
                     (this.i * 92), CString('ascii')),
)

mstudioiklink_t = Struct(
    'bone' / Int32sl,
    'kneeDir' / Vector,
    'unused0' / Vector,
)

mstudioikchain_t = Struct(
    'i' / Index,

    'sznameindex' / Int32sl,
    'linktype' / Int32sl,
    'numlinks' / Int32sl,
    'linkindex' / Int32sl,

    'name' / Pointer(this.sznameindex + this._.ikchainindex +
                     (this.i * 16), CString('ascii')),
    'links' / Pointer(this.linkindex + this._.ikchainindex +
                      (this.i * 16), mstudioiklink_t[this.numlinks])
)

mstudioiklock_t = Struct(
    'chain' / Int32sl,
    'flPosWeight' / Float32l,
    'flLocalQWeight' / Float32l,
    'flags' / Int32sl,
    'unused' / Int32sl[4],
)

mstudioikrule_t = Struct(
    'index' / Int32sl,
    'type' / Int32sl,
    'chain' / Int32sl,
    'bone' / Int32sl,
    'slot' / Int32sl,
    'height' / Float32l,
    'radius' / Float32l,
    'floor' / Float32l,
    'pos' / Vector,
    'q' / Quaternion,
    'compressedikerrorindex' / Int32sl,
    'unused2' / Int32sl,
    'iStart' / Int32sl,
    'ikerrorindex' / Int32sl,
    'start' / Float32l,
    'peak' / Float32l,
    'tail' / Float32l,
    'end' / Float32l,
    'unused3' / Float32l,
    'contact' / Float32l,
    'drop' / Float32l,
    'top' / Float32l,
    'unused6' / Int32sl,
    'unused7' / Int32sl,
    'unused8' / Int32sl,
    'szattachmentindex' / Int32sl,
    'unused' / Int32sl[7],
)

mstudiolocalhierarchy_t = Struct(
    'iBone' / Int32sl,
    'iNewParent' / Int32sl,
    'start' / Float32l,
    'peak' / Float32l,
    'tail' / Float32l,
    'end' / Float32l,
    'iStart' / Int32sl,
    'localanimindex' / Int32sl,
    'unused' / Int32sl[4],
)
mstudioanim_t = Struct(
    'bone' / Byte,
    'flags' / Byte,
    'nextoffset' / Int16sl,
)
mstudiovertanim_t = Struct(
    'index' / Int16ul,
    'speed' / Byte,
    'side' / Byte,
)
mstudioanimblock_t = Struct(
    'datastart' / Int32sl,
    'dataend' / Int32sl,
)
mstudioanimsections_t = Struct(
    'animblock' / Int32sl,
    'animindex' / Int32sl,
)
mstudioanimdesc_t = Struct(
    'i' / Index,

    'baseptr' / Int32sl,
    'sznameindex' / Int32sl,
    'fps' / Float32l,
    'flags' / Int32sl,
    'numframes' / Int32sl,

    'nummovements' / Int32sl,
    'movementindex' / Int32sl,  # mstudiomovement_t

    'unused1' / Int32sl[6],

    'animblock' / Int32sl,
    'animindex' / Int32sl,  # mstudioanim_t

    'numikrules' / Int32sl,
    'ikruleindex' / Int32sl,

    'animblockikruleindex' / Int32sl,

    'numlocalhierarchy' / Int32sl,
    'localhierarchyindex' / Int32sl,

    'sectionindex' / Int32sl,
    'sectionframes' / Int32sl,

    'zeroframespan' / Int16sl,
    'zeroframecount' / Int16sl,
    'zeroframeindex' / Int32sl,

    'name' / Pointer(this.sznameindex + this._.localanimindex + \
                     (this.i * 96), CString('ascii')),
)

mstudioautolayer_t = Struct(
    'iSequence' / Int16sl,
    'iPose' / Int16sl,
    'flags' / Int32sl,
    'start' / Float32l,
    'peak' / Float32l,
    'tail' / Float32l,
    'end' / Float32l,
)

mstudiomodelgroup_t = Struct(
    'i' / Index,
    'szlabelindex' / Int32sl,  # todo?
    'sznameindex' / Int32sl,

    'name' / Pointer(this.sznameindex + this._.includemodelindex +
                     (this.i * 8), CString('ascii')),
)
studiohdr2_t = Struct(
    'numsrcbonetransform' / Int32sl,
    'srcbonetransformindex' / Int32sl,
    'illumpositionattachmentindex' / Int32sl,
    'flMaxEyeDeflection' / Float32l,
    'linearboneindex' / Int32sl,
    'sznameindex' / Int32sl,
    'm_nBoneFlexDriverCount' / Int32sl,
    'm_nBoneFlexDriverIndex' / Int32sl,
)

skinfamily = Array(this._.numskinref, Int16sl)
skintable = Struct('families' / skinfamily[this._.numskinfamilies])

studiohdr_t = Struct(
    'id' / Const(b'IDST'),
    'version' / Const(48, Int32sl),
    'checksum' / Int32sl,

    'name' / PaddedString(64, "ascii"),
    'dataLength' / Int32sl,
    'eyeposition' / Vector,
    'illumposition' / Vector,
    'hull_min' / Vector,
    'hull_max' / Vector,
    'view_bbmin' / Vector,
    'view_bbmax' / Vector,
    'flags' / Int32sl,

    'numbones' / Int32sl,  # !ok
    'boneindex' / Int32sl,  # !ok

    'RemapSeqBone' / Int32sl,
    'RemapAnimBone' / Int32sl,

    'numhitboxsets' / Int32sl,  # !ok
    'hitboxsetindex' / Int32sl,  # !ok

    'numbonecontrollers' / Int32sl,  # todo
    'bonecontrollerindex' / Int32sl,

    'numlocalanim' / Int32sl,  # todo
    'localanimindex' / Int32sl,

    'numlocalseq' / Int32sl,
    'localseqindex' / Int32sl,

    'numtextures' / Int32sl,  # !ok
    'textureindex' / Int32sl,  # !ok
    'numcdtextures' / Int32sl,  # !ok
    'cdtextureindex' / Int32sl,  # !ok
    'numskinref' / Int32sl,  # !ok
    'numskinfamilies' / Int32sl,  # !ok
    'skinindex' / Int32sl,  # !ok
    'numbodyparts' / Int32sl,  # !ok
    'bodypartindex' / Int32sl,  # !ok
    'numlocalattachments' / Int32sl,  # !ok
    'localattachmentindex' / Int32sl,  # !ok
    'numlocalnodes' / Int32sl,
    'localnodeindex' / Int32sl,
    'localnodenameindex' / Int32sl,
    'numflexdesc' / Int32sl,
    'flexdescindex' / Int32sl,
    'numflexcontrollers' / Int32sl,
    'flexcontrollerindex' / Int32sl,
    'numflexrules' / Int32sl,
    'flexruleindex' / Int32sl,
    'numikchains' / Int32sl,  # !ok
    'ikchainindex' / Int32sl,  # !ok
    'nummouths' / Int32sl,
    'mouthindex' / Int32sl,
    'numlocalposeparameters' / Int32sl,  # !ok
    'localposeparamindex' / Int32sl,  # !ok
    'surfacepropindex' / Int32sl,
    'keyvalueindex' / Int32sl,
    'keyvaluesize' / Int32sl,
    'numlocalikautoplaylocks' / Int32sl,
    'localikautoplaylockindex' / Int32sl,
    'mass' / Float32l,
    'contents' / Int32sl,
    'numincludemodels' / Int32sl,  # !ok
    'includemodelindex' / Int32sl,  # !ok
    'szanimblocknameindex' / Int32sl,
    'numanimblocks' / Int32sl,
    'animblockindex' / Int32sl,
    'bonetablebynameindex' / Int32sl,
    'pVertexBase' / Int32sl,
    'pIndexBase' / Int32sl,
    'constdirectionallightdot' / Byte,
    'rootLOD' / Byte,
    'numAllowedRootLODs' / Byte,
    'unused1' / Byte,
    'unused4' / Int32sl,
    'numflexcontrollerui' / Int32sl,
    'flexcontrolleruiindex' / Int32sl,
    'flVertAnimFixedPointScale' / Float32l,
    'unused3' / Int32sl,
    'test1' / Int32sl,
    'test2' / Int32sl,
    'studiohdr2index' / Int32sl,
    'unused2' / Int32sl,

    'studiohdr2_t' / Pointer(this.studiohdr2index, studiohdr2_t),
    'textures' / Pointer(this.textureindex,
                        mstudiotexture_t[this.numtextures]),
    'cdtextures' / Pointer(this.cdtextureindex,
                          mstudiocdtexture_t[this.numcdtextures]),
    'skintable' / Pointer(this.skinindex, skintable),
    
    'bodyparts' / Pointer(this.bodypartindex,
                         mstudiobodyparts_t[this.numbodyparts]),
    'attachments' / Pointer(this.localattachmentindex,
                           mstudioattachment_t[this.numlocalattachments]),
    'bones' / Pointer(this.boneindex, mstudiobone_t[this.numbones]),
    'bonecontrollers' / Pointer(this.bonecontrollerindex,
                               mstudiobonecontroller_t[this.numbonecontrollers]),
    'hitboxsets' / Pointer(this.hitboxsetindex,
                          mstudiohitboxset_t[this.numhitboxsets]),
    'localposeparams' / Pointer(this.localposeparamindex,
                               mstudioposeparamdesc_t[this.numlocalposeparameters]),
    'ikchains' / Pointer(this.ikchainindex,
                        mstudioikchain_t[this.numikchains]),
    'includemodels' / Pointer(this.includemodelindex,
                             mstudiomodelgroup_t[this.numincludemodels]),
    #    'anims' / Pointer(this.localanimindex,
#                     mstudioanimdesc_t[this.numlocalanim]),
)
