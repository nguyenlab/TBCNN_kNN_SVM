import gl
import pycparser

gl.reConstruct= False # reconstruct For, While, DoWhile
gl.ignoreDecl = False # Ignore declaration branches
# import main_TBCNN_Sib as NetConstruct
# import main_TBCNN as NetConstruct
import main_RNN as NetConstruct
# import main_RNN_Sib as NetConstruct
text ='''
int a = b+3;
'''

# text ='''
# int main()
# {
#     int a = 3;
# }
# '''

#
# text ='''
# int main()
# {
#     int sum =0;
#     for (int i=0; i<10; i++)
#         sum = sum + i;
# }
# '''

parser = pycparser.c_parser.CParser()
ast = parser.parse(text=text)  # Parse code to AST
if gl.reConstruct:  # reconstruct braches of For, While, DoWhile
    ast.reConstruct()
print 'AST:'
ast.show()
print '\n\nNetworks:'
layers = NetConstruct.InitNetbyText(text = text)
print 'Totally:', len(layers), 'layer(s)'
for l in layers:
    if hasattr(l,'bidx') and l.bidx is not None:
        print l.name, '\tBidx', l.bidx[0], '\tlen biases=', len(l.bidx)
    else:
        print l.name
    # print "    Up:"
    # for c in l.connectUp:
    #     if hasattr(c,'Widx'):
    #         print "        ", c.xlayer.name, " -> ", c.ylayer.name, \
    #             '(xnum= ', c.xnum, ', ynum= ', c.ynum,'), weights = ', len(c.Widx)
    #     else:
    #         print "        ", c.xlayer.name, " -> ", c.ylayer.name, \
    #             '(xnum= ', c.xnum, ', ynum= ', c.ynum, ')'

    print "    Down:"
    for c in l.connectDown:
        if hasattr(c,'Widx'):
            print "        ", c.xlayer.name, " -> ", '|', \
                '(xnum= ', c.xnum, ', ynum= ', c.ynum,'), weights = ', len(c.Widx)
        else:
            print "        ", c.xlayer.name, " -> ", '|', \
                '(xnum= ', c.xnum, ', ynum= ', c.ynum, ')'

