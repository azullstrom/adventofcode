def get_marker(buffer, signal_length):
    marker = 0
    for i in range(len(buffer)):
        temp_arr = []
        for j in range(i, i + signal_length):
            if buffer[j] not in temp_arr:
                temp_arr.append(buffer[j])
        if len(temp_arr) == signal_length:
            marker = i + signal_length
            break
    return marker


if __name__ == '__main__':
    buffer = "sbpbwwrlwrwggscsfcsshsvhshphttzctztfflddvbvcbcvbcbnbrrstsspsvpvllncccqssqdssnsmshmshhtssbzzlplffzppddmhhwnhntnjtnjtnnqggjdgjdjrjffsdfsfbsffhtthwwfssqpspllcvcdvvfvfzfbzzgpglpgpmppfsfdfbfvvfjfsjjvqqbvqbvqbvvlvglvglvljvjzvvqcvqcqjcqqpddqbqcqrqmmvnvbnnfqnncznccqjcqqjzzwlltrrmmlwlllbjlblzlddfdmmscmsspfssqggbsbsjjdqdqgqgqbqdqrqlrrltttghthrtrwrdrnrfnfvftvtsvtvwtvwttvqtvtccqtqmqggwhhhlzhhrwwbwqwbbfrrmddwhdwdnwdwbdwwsswtwnnvvdggbbtwbbwllgffqpffpgpgmpmmjqqmpmffjgfgrffdzzspzptzzdszszbsbsbsvsbbhsbsbddnhhrqqcwwblbwlwnnthtsshmshmhgmgqgjqqpccfvcvbbbnllgmlgmmbnmnlmlzlffrrrgssmcmddnpdndtntrrqdqldldbbtppvddgndnwwctwccpbpffngnsgshggphggtssgngtnthtllzflzflzfzrfftgtstppghgnnpggrdgdnnswwccljlflwwgzgcgrrhssbwbllblnlvlddsffgrrnbbmsmmmhjmjvmjvmjmqqpdqppltlflmfmssqcqsqvsvsggpglplslggqtggmsmmmgffrccrvvsdvdvfddprdprrwjrjcjjmlmrmqmggqgdqdwdsdwwwgfwfddrcdcvcmmjbbmrrhlrrwcwvcclttwbwttgffnmnjmjdmmmlqmqrrlblplccdbcbwcbcpphpqpqlqrllqwwjsjgjbjqbbmcmzmrrqtrqqmcmmnjmjbbtnnbbjdjzzvbzvzjzdjzjrzzfzfbbmnmdnnzppmbpbhbdbvvqnqqnqrnrzrhhrddbqdqpqqwgwlglplglslhhpjpdjdjgddnppmvppjddczccgsccdsccbcvczccnbnmmsnsmmrwmwbmbbcpbbwbppzggdnnnzmnzzvrvcrvcvcrvrnrzzqzmzttjhhnffqggnqqwzwfzfwzwfwcwnccwgcwgcgqcgqcggzgwgfwgfffjttjddwswqqnttqwqsqhhcmchcscbbnwnlwlrlppqnnwjnjtntrtdtbbmzzrmzrzvrzvrzzwqwqllccnffvmmfmvmzzfttnnzttrbttdvvhdhzhzhvzzfsfszsvsttrqqdlldflfjjnqjjbhhqhzhcchppzsznntdntdddqqwjqjqmmgnnhrhjhnjnznwwdpplzzfzztbzzbmzmbbgjgtjtqjqpqhqgqhhtztpzpmzmjmhhjwwjsspbssvdsvsgvssghgvglgtltgllmhmtmhttfgglwgllpvpgpspzzhnnzcnzzldzdmzmlzzwtwhhlfhhvthhjdjsdsmddgzzsjjnznjnmjjgdgtdtzdtdvtddzwzgwwqvqccwrrrvddbtdbbshbhssnvsnvssswcwjcjlltvvltvvdsdqdsswlwttzfzhzjjgjsgjgttbccsvcscllbfbzzwwwznwwtzwzjzwjjgqjqrjrdjrddzsznsznzpzszhzzspzzbzrzhhsbspsqpqqqpddhdcdldttlccjrjsrsfftfdfrrtntpnpsnnwjnwnznpzzlqqlmqlmmcddlqqzssglsglssprmnvltqhslvqmvszjtvtwqjcdngjmftnhwvjdvtwwhtnsdmvjdspnhnlmjgnmwlspcvpdmlsrnbbzlmwwrslssmcbggmfvgzsnpnlnzdqsbhcfjdccrspnzfmhbvwstvccvqqjlwhpnlrrwszjnrtdfzwrwlzwvdvbzbvltdpfwrjlslmrctwvbbvdrctgtgwtwpjjghhvdsqhplfrsjqlgsrbfgwdjlzdpdljtvjmpwqqbghndqnvjhngtpnpvzfbtchncwdqjhmzjlpdggbdcqrfjlwvczvpspljqmpgtrsvwwhqncfvfrwbnvsfjqlsjdlrqzmlqjgcpghhgzfhjcglllnhtmchrrptbzhqnfntgqbfstrvpsqsvqvcvpgjnchbvmgtgzqfrqcjrvldzghdfrvllrtfcwnsmmgdrcbjmdqgbfwmpwhfjmnbqrbvqvnmjlqtsjqvhzpdsgbjpjngmzbgnznvjqprfvwzjrfrwfdqrtlcgqqlvrzwmqwjbdvprvpwvdcrfdrcttnmnvjfrsrrmjgfjdmpdpnfsrwnprtdpvdmdwssvjrqtlcvpgrqgqqqffvvssbmghzjrzrzlcrnfjtdbvwsjzfvcrsmgqbcrdrjwdwbltffwbgjwtgtdblmlhvhlcpgdmpcztmpmgjghqpwzwtpnmnmgnqqrrtwczgmgtdbgdqtpnlbnzhshsfzsmrztffrmlsgqcprbjpqwjlqgwvctpmpshgzbzsjgqhzvsrjfwplvjbvltrlfldvsmlppcmsfrbbctggmqmjnhppstzrcfjtdgfwrrnmlvjphwtlqtjqcntjtzvgjtwvthjfbgpwhlrzdqncmggvgthmgjvrbnzbndsldnlcgtcqbqdnnbnqhvtpfnrclttfwcpnqscjbzdvbqrrsbzpdfhjllbjwsltjpmdnbrrzvhvzzqnlbglsjrnjbqffnnzmldfvtvmldfsztrnpcjgblsdhzfzmfqzlfrtslglhfvszppptjnjqcdmjcwqmfzhnqbfhslwhvtjfvcftzsphvghvtjjswpwghnfngmzddbwwqddsphvhcrwtthsjfswfqbvdsqghmrspdldfqmchnnrcdvjsclcnlsncsplchvzrwqbtvvqlqspftrwmjcbgpzbsmnfccbzgnhqsfjgmmsqsscdscfjbrmmtjbsphhlrlsgbllrptqrcgnqchzfddjwlldsbpcnzfbspfpchclqfbbtjpmtmtjthcdvwhrtqbgmgldcgcnmmhtbnqpzzcwlrscbzcqjzgztwjrnbmsnqtcllznlctzrntftspmnvhtfwbljnmrwsstvbmwclqrfpmwvjphrwddzdwtlfcvzlvqdmzhnvslfnfjhvdndlgbvvzbztpwvqzbzsbtqpqfmgqfgpzctfrqfjwmsnmlfqbgrlmncntcbshjhdcbqnvznhtcgcmmhnsbwpzbvtqbntwgflhjgmvvfhdbwfqmnfjlzdvvnpmvjrdfdnrhpbtllhbtbswwvrbwjgnqpbgnfrjtvbczbpmrcbwdlhztzssnwshjmmcqchptrtchrqncdgdtmwrlnmmwqlzqswwwvpngvwcphgnzrhpprjnbldscvwlqdjwnhjrnscdwlnhnsbwgzjtgvzdgqcjcgvrdhntszhdnjsbbrfphlmdlldjdslbjnnsfbmcnvtlczmtnhrwblnbrdptcpmsbwqptgmwzsqnmmchwnnrvrlfsrglfzzqbnzmpdtnhhbmfqvsrsdsctvhqwfgbtvhbbrsrqmrvvplrnbfnbdmrvzpgctdtglndhcqnllvvcppgfbwjrpqcbghlqdbmpzwrqpmvwddqgthlmzmdsvzdfsmgzltbsvphctzgjsmqvgjlsbgnvmgprbcsfhgrtbwtnnrsqcwfzrhlgjcwcfrjhffrvrvtnpczvwvjnnhfdgcppnnjjpttptcbmdqvgdbhdmlqgcqsrnbcrbtcgzbvgmhbnwzsgnwzbhdqqmvtpssvlvsttgnmcclqnjcgjnvtdggrcwsgbpjljgzgtllsnfvfshtbbpwrjhzvzswlfdvhbpngvgddcmhbzqcvnjhfsqpnvvsdvdtmqlqpzcgsnwlflnqprbqnwdqchjvsptbtrvtzvhrmrvznfpzmcsgnqtdvghhzwrrwvqwrztvdbjjtfchpftdcbthpfdczwchpptwzdpswvbhppdphgvpfzhprpqtnprgfmdnqrbrdlclcmhrdfrcdhwpcqhnbwmhrrgnctpvsqmphcwwvlmslszhdz"

    # Part 1
    print(get_marker(buffer, 4))
    # Part 2
    print(get_marker(buffer, 14))
